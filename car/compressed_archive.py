from .file import File


class CARFile:
    def __init__(self, file: File) -> None:
        self.file: File = file
