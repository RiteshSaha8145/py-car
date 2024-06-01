from pycar.car import folder_to_dag, CARv1Writer
import pytest


def test_carv1_file_writer():
    try:
        with CARv1Writer(
            None,
            "dummy_folder.car",
            unixfs=True,
            max_children=11,
        ) as c:
            folder_to_dag(car_writer=c, folder_path="./statics", chunk_size=1)
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected exception: {e}")
