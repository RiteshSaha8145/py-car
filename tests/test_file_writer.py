from pycar.car import CARv1Writer
from pycar.file_types import BinaryFile
import pytest

from pathlib import Path


@pytest.fixture
def dummy_file_path():
    # Get the path to the current test file
    test_file_path = Path(__file__).parent
    # Construct the full path to the dummy file
    return test_file_path / "statics" / "dummy"


def test_carv1_file_writer(dummy_file_path):
    try:
        with open(dummy_file_path, "rb") as f:
            with CARv1Writer(
                BinaryFile(bufferedReader=f, chunkSize=1, metadata={"name": "dummy"}),
                "file.car",
                unixfs=True,
                max_children=1024,
            ) as c:
                c.get_car()
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected exception: {e}")
