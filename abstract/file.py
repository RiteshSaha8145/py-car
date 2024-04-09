from collections.abc import Iterator
from abc import abstractmethod
from typing import BinaryIO, Optional


class File(Iterator):
    """
    An abstract base class representing a generic file.

    This class defines the interface for working with files in a generic way.
    The abstract methods, `__next__` and `reset`, must be implemented by concrete
    subclasses to define file iteration behavior.

    Attributes:
        bufferedReader (BinaryIO): The binary reader for the file.
        chunkSize (Optional[int]): The size of each chunk to read, if applicable.
        metadata (Optional[dict]): Metadata associated with the file.
    """

    def __init__(
        self,
        bufferedReader: BinaryIO,
        chunkSize: int,
        metadata: Optional[dict],
    ):
        """
        Initializes the File object.

        Args:
            bufferedReader (BinaryIO): The binary reader for the file.
            chunkSize (int): The size of each chunk to read, if applicable.
            metadata (Optional[dict]): Metadata associated with the file.
        """
        self.bufferedReader = bufferedReader
        self.chunkSize = chunkSize
        self.metadata = metadata

    @abstractmethod
    def reset(self):
        """
        Reset the file pointer to the beginning of the file.

        This method should be implemented by concrete subclasses to define
        how the file pointer is reset.
        """
        ...
