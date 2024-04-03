from car import CARv1Writer
from file_types import BinaryFile

if __name__ == "__main__":
    with open("sample.html", "rb") as f:
        with CARv1Writer(BinaryFile(f, 262144), "test.car") as c:
            c.get_flat_car()
