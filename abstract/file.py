from collections.abc import Iterator


class File(Iterator):
    """
    An abstract base class representing a generic file.

    This class defines the interface for working with files in a generic way.
    The abstract method, `__next__`, must be implemented by concrete
    subclasses to define file iteration behavior.
    """

    ...
