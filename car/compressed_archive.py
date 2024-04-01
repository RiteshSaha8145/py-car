from ..file_types.binary_file import BinaryFile
from ..protobufs.ipld_dag_pb2 import PBLink, PBNode
from ..protobufs.unixfs_pb2 import Data
from contextlib import AbstractContextManager
from multiformats import CID, multihash, varint
from typing import BinaryIO, Optional, Type, Tuple, List
from types import TracebackType
import dag_cbor


class CARv1Reader(AbstractContextManager):
    def __init__(self, file: BinaryFile):
        self.file = file


class CARv1Writer(AbstractContextManager):
    def __init__(self, file: BinaryFile, name: str):
        self.file = file
        self.name = name
        self.bufferedWriter: BinaryIO = open(name, "rb")

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
        /,
    ) -> Optional[bool]:
        if self.bufferedWriter:
            self.bufferedWriter.close()
            return True
        return False

    def __gen_cid(self, data: bytes, codec: str):
        hash_value: bytes = multihash.digest(data, "sha2-256")
        return CID("base32", version=1, codec=codec, digest=hash_value)

    def __get_block(self, cid: CID, data: bytes):
        cid = bytes(cid)
        return varint.encode(len(cid) + len(data)) + cid + data

    def __to_flat_dag(self) -> Tuple[CID, List[PBLink], bytes]:
        links: list = []
        total_size: int = 0
        for i, data in enumerate(self.file):
            cid = self.__gen_cid(data=data, codec="raw")
            link = PBLink()
            link.Hash = bytes(cid)
            link.Name = f"Links/{i}"
            link.Tsize = len(data)
            links.append(link)
            total_size += len(data)
            links.append(link)

        unixfs = Data()
        unixfs.Type = Data.DataType.File
        unixfs.blocksizes.extend(total_size)

        pbnode = PBNode()
        pbnode.Links.extend(links)
        pbnode.Data = unixfs.SerializeToString()
        pbnode_bytes = pbnode.SerializeToString()

        root_cid = self.__gen_cid(data=pbnode_bytes, codec="dag-pb")
        return (root_cid, links, pbnode)

    def to_flat_dag(self) -> CID:
        self.file.bufferedReader.seek(0)
        root_cid, links, root_node = self.__to_flat_dag()

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
