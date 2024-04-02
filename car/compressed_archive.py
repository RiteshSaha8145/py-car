from file_types import BinaryFile
from protobufs import PBNode, PBLink, Data
from contextlib import AbstractContextManager
from multiformats import CID, multihash, varint
from typing import BinaryIO, Optional, Type, Tuple, List
from types import TracebackType
import dag_cbor


class CARv1Reader(AbstractContextManager):
    def __init__(self, file: BinaryFile):
        self.file = file


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

    def __init__(self, file: BinaryFile, name: str):
        self.file = file
        self.name = name
        self.bufferedWriter: BinaryIO = open(name, "wb")

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
        if self.bufferedWriter:
            self.bufferedWriter.close()
            return True
        return False

    def __gen_cid(self, data: bytes, codec: str):
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

    def __get_block(self, cid: CID, data: bytes):
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

    def to_flat_dag(self) -> CID:
        """
        Convert the CARv1 file data to a flat DAG and write it to the buffered writer.

        Returns:
            CID: The root CID of the flat DAG.
        """
        root_cid, links, root_node = self.__to_flat_dag()
        self.file.bufferedReader.seek(0)

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
