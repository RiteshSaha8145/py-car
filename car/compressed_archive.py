from abstract import File
from protobufs import PBNode, PBLink, Data
from contextlib import AbstractContextManager
from multiformats import CID, multihash, varint
from typing import BinaryIO, Optional, Type, Tuple, List, Generator
from types import TracebackType
import dag_cbor
from collections.abc import Iterator
import tempfile
import shutil


class CARv1Reader(AbstractContextManager, Iterator):
    """
    Context manager for reading data from a CARv1 file.

    Args:
        file (str): The path to the CARv1 file to read from.

    Attributes:
        file (str): The path to the CARv1 file being read from.
        bufferedReader (BinaryIO): The buffered reader for the CARv1 file.
    """

    def __init__(self, file: str):
        self.file = file
        self.bufferedReader = open(file, "rb")

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
        /,
    ) -> Optional[bool]:
        """
        Exit the context manager and close the buffered reader.

        Args:
            exc_type (Optional[Type[BaseException]]): The type of the exception, if any.
            exc_value (Optional[BaseException]): The exception value, if any.
            traceback (Optional[TracebackType]): The traceback, if any.

        Returns:
            Optional[bool]: True if the buffered reader was closed successfully, False otherwise.
        """
        if self.bufferedReader:
            self.bufferedReader.close()
            return True
        return False


class CARv1Writer(AbstractContextManager):
    """
    Context manager for writing data to a CARv1 file.

    Args:
        file (BinaryFile): The binary file object to write to.
        name (str): The name of the CARv1 file to create.

    Attributes:
        file (BinaryFile): The binary file object being written to.
        name (str): The name of the CARv1 file being created.
        bufferedWriter (BinaryIO): The buffered writer for the CARv1 file.
    """

    def __init__(self, file: File, name: str, unixfs: bool = False):
        self.file = file
        self.name = name
        self.bufferedWriter: BinaryIO = open(name, "wb")
        self.unixfs = unixfs

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
        /,
    ) -> Optional[bool]:
        """
        Exit the context manager and close the buffered writer.

        Args:
            exc_type (Optional[Type[BaseException]]): The type of the exception, if any.
            exc_value (Optional[BaseException]): The exception value, if any.
            traceback (Optional[TracebackType]): The traceback, if any.

        Returns:
                Optional[bool]: True if the buffered writer was closed successfully, False otherwise.
        """
        self.bufferedWriter.close()
        return True

    def __gen_cid(self, data: bytes, codec: str) -> CID:
        """
        Generate a CID for the given data.

        Args:
            data (bytes): The data to calculate the CID for.
            codec (str): The codec to use for the CID.

        Returns:
            CID: The generated CID.
        """
        hash_value: bytes = multihash.digest(data, "sha2-256")
        return CID("base32", version=1, codec=codec, digest=hash_value)

    def __get_block(self, cid: CID, data: bytes) -> bytes:
        """
        Get a block with the given CID and data.

        Args:
            cid (CID): The CID for the block.
            data (bytes): The data for the block.

        Returns:
            bytes: The block data.
        """
        cid = bytes(cid)
        return varint.encode(len(cid) + len(data)) + cid + data

    def __get_raw_node(self) -> Generator[Tuple[bytes, CID], None, None]:
        for raw_data in self.file:

            codec, block = "raw", raw_data
            if self.unixfs:
                unixfs_block = Data()
                unixfs_block.Type = Data.DataType.Raw
                unixfs_block.Data = raw_data
                unixfs_block.blocksizes.extend([len(raw_data)])

                pbnode = PBNode()
                pbnode.Data = unixfs_block.SerializeToString()

                codec, block = "dag-pb", pbnode.SerializeToString()

            cid = self.__gen_cid(data=block, codec=codec)
            block = self.__get_block(cid=cid, data=block)

            self.bufferedWriter.write(block)

            yield (block, cid)

    def __get_file_node(self) -> Generator[Tuple[bytes, CID], None, None]:
        unixfs = Data()
        unixfs.Type = Data.DataType.File

        pbnode = PBNode()
        for i, block in enumerate(self.__get_raw_node()):
            data, cid = block

            link = PBLink()
            link.Hash = bytes(cid)
            link.Name = f"Links{i}"
            link.Tsize = len(data)

            pbnode.Links.extend([link])
            unixfs.blocksizes.extend([len(data)])

        pbnode.Data = unixfs.SerializeToString()
        pbnode_bytes = pbnode.SerializeToString()

        cid = self.__gen_cid(data=pbnode_bytes, codec="dag-pb")
        pbnode_block = self.__get_block(cid=cid, data=pbnode_bytes)
        self.bufferedWriter.write(pbnode_block)

        yield (pbnode_block, cid)

    def get_car(self) -> CID:
        cid = [cid for _, cid in self.__get_file_node()][0]
        encoded_root_node = dag_cbor.encode({"roots": [cid], "version": 1})
        header = varint.encode(len(encoded_root_node)) + encoded_root_node
        self.bufferedWriter.flush()

        with tempfile.NamedTemporaryFile(mode="wb", delete=False) as tmp_file:
            tmp_file.write(header)

            with open(self.name, "rb") as original_file:
                while True:
                    data = original_file.read(self.file.chunkSize)
                    if not data:
                        break
                    tmp_file.write(data)

        shutil.move(tmp_file.name, self.name)
        return cid

    def __to_flat_dag(self) -> Tuple[CID, List[PBLink], bytes]:
        """
        Convert the file data into a flat DAG structure.

        Returns:
            Tuple[CID, List[PBLink], bytes]: The root CID, list of links, and root node bytes.
        """
        links: list = []
        total_sizes: list = []
        for i, data in enumerate(self.file):
            cid = self.__gen_cid(data=data, codec="raw")
            link = PBLink()
            link.Hash = bytes(cid)
            link.Name = f"Links/{i}"
            link.Tsize = len(data)
            links.append(link)
            total_sizes.append(len(data))

        unixfs = Data()
        unixfs.Type = Data.DataType.File
        unixfs.blocksizes.extend(total_sizes)

        pbnode = PBNode()
        pbnode.Links.extend(links)
        pbnode.Data = unixfs.SerializeToString()
        pbnode_bytes = pbnode.SerializeToString()

        root_cid = self.__gen_cid(data=pbnode_bytes, codec="dag-pb")
        return (root_cid, links, pbnode_bytes)

    def get_flat_car(self) -> CID:
        """
        Convert the CARv1 file data to a flat DAG and write it to the buffered writer.

        Returns:
            CID: The root CID of the flat DAG.
        """
        root_cid, links, root_node = self.__to_flat_dag()
        self.file.reset()

        encoded_header = dag_cbor.encode({"roots": [root_cid], "version": 1})
        header = (
            varint.encode(len(encoded_header))
            + encoded_header
            + self.__get_block(root_cid, root_node)
        )

        self.bufferedWriter.write(header)

        for i, data in enumerate(self.file):
            block = self.__get_block(cid=links[i].Hash, data=data)
            self.bufferedWriter.write(block)
        return root_cid
