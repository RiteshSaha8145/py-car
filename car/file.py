from abc import ABC, abstractmethod


class File(ABC):
    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self):
        ...

    @abstractmethod
    def encode(self):
        ...
