from pycar.car import folder_to_dag, CARv1Writer
import pytest
from pathlib import Path


@pytest.fixture
def dummy_folder_path():
    # Get the path to the current test file
    test_file_path = Path(__file__).parent
    # Construct the full path to the dummy file
    return test_file_path / "statics" / "dummy_folder"


def test_carv1_file_writer(dummy_folder_path):
    try:
        with CARv1Writer(
            None,
            "dummy_folder.car",
            unixfs=True,
            max_children=1024,
        ) as c:
            folder_to_dag(car_writer=c, folder_path=dummy_folder_path, chunk_size=1)
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected exception: {e}")
