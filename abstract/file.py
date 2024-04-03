from collections.abc import Iterator
from abc import abstractmethod


class File(Iterator):
    """
    An abstract base class representing a generic file.

    This class defines the interface for working with files in a generic way.
    The abstract methods, `__next__` `reset`, must be implemented by concrete
    subclasses to define file iteration behavior.
    """

    @abstractmethod
    def reset(self):
        ...
