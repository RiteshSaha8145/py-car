from collections.abc import Iterator
from abc import abstractmethod
from typing import BinaryIO, Optional


class File(Iterator):
    """
    An abstract base class representing a generic file.

    This class defines the interface for working with files in a generic way.
    The abstract methods, `__next__` `reset`, must be implemented by concrete
    subclasses to define file iteration behavior.
    """

    def __init__(self, bufferedReader: BinaryIO, chunkSize: Optional[int]):
        self.bufferedReader = bufferedReader
        self.chunkSize = chunkSize

    @abstractmethod
    def reset(self):
        ...
