from ..abstract.file import File
from contextlib import AbstractContextManager
from multiformats import CID, multihash, varint
from typing import BinaryIO, Optional, Type
from types import TracebackType


class CARv1Reader(AbstractContextManager):
    def __init__(self, file: File):
        self.file = file


class CARv1Writer(AbstractContextManager):
    def __init__(self, file: File, name: str):
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
