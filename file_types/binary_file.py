from abstract.file import File
from typing import BinaryIO, Optional


class BinaryFile(File):
    """
    This class represents a binary file and provides an iterator over chunks
    of binary data from the file.

    Attributes:
        bufferedReader (BinaryIO): The binary input stream representing the file.
        chunkSize (Optional[int]): The size of each chunk of data to read.
    """

    def __init__(self, bufferedReader: BinaryIO, chunkSize: Optional[int] = 1024):
        """
        Initializes a BinaryFile object.

        Args:
            bufferedReader (BinaryIO): A binary input stream representing the file.
            chunkSize (Optional[int], optional): The size of each chunk of data to read
                from the file. Defaults to 1024 bytes.
        """
        self.bufferedReader = bufferedReader
        self.chunkSize = chunkSize

    def __next__(self):
        """
        Iterates over chunks of binary data from the file.

        Returns:
            bytes: A chunk of binary data from the file.

        Raises:
            StopIteration: If the end of the file has been reached.
        """
        data: bytes = self.bufferedReader.read(self.chunkSize)
        if not data:
            raise StopIteration
        return data
