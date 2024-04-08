from tempfile import NamedTemporaryFile
from shutil import copyfileobj, move


def prepend_data_to_file(file_name: str, data: bytes) -> None:
    with NamedTemporaryFile(mode="wb", delete=False) as tmp_file:
        tmp_file.write(data)

        with open(file_name, "rb") as original_file:
            copyfileobj(original_file, tmp_file)

    move(tmp_file.name, file_name)
