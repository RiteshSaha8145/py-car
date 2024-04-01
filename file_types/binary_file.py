from ..abstract.file import File
from typing import BinaryIO


class BinaryFile(File):
    def __init__(self, bufferedReader: BinaryIO, chunkSize: int = 1024):
        self.bufferedReader = bufferedReader
        self.chunkSize = chunkSize

    def __iter__(self):
        data: bytes = self.bufferedReader.read(self.chunkSize)
        if not data:
            raise StopIteration
        return data
