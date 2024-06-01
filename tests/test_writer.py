from pycar.car import CARv1Writer
from pycar.file_types import BinaryFile
import pytest


def test_carv1_writer():
    try:
        with open("requirements.txt", "rb") as f:
            with CARv1Writer(
                BinaryFile(
                    bufferedReader=f, chunkSize=1, metadata={"name": "requirements.txt"}
                ),
                "test.car",
                unixfs=True,
                max_children=11,
            ) as c:
                c.get_car()
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected exception: {e}")
