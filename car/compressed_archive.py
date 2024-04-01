from ..abstract.file import File
from contextlib import AbstractContextManager


class CARv1Reader(AbstractContextManager):
    def __init__(self, file: File):
        self.file = file


class CARv1Writer(AbstractContextManager):
    def __init__(self, file: File, name: str):
        self.file = file
        self.name = name
