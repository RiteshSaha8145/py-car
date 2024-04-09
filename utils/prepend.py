from tempfile import NamedTemporaryFile
from shutil import copyfileobj, move


def prepend_data_to_file(file_name: str, data: bytes) -> None:
    """
    Prepends the given binary data to the beginning of the specified file.

    Args:
        file_name (str): The path to the file to prepend data to.
        data (bytes): The binary data to prepend to the file.

    Raises:
        IOError: If there is an issue reading or writing to the file.

    Note:
        This function works by creating a temporary file in the same directory
        as the original file. It then copies the contents of the original file
        into the temporary file, followed by writing the provided data to the
        temporary file. Afterward, it replaces the original file with the
        temporary file. This approach is used to efficiently prepend data to
        large files without reading the entire file into memory.

    Example:
        >>> prepend_data_to_file("example.txt", b"Hello, ")
        # Prepends "Hello, " to the beginning of example.txt
    """
    with NamedTemporaryFile(mode="wb", delete=False) as tmp_file:
        tmp_file.write(data)

        with open(file_name, "rb") as original_file:
            copyfileobj(original_file, tmp_file)

    move(tmp_file.name, file_name)
