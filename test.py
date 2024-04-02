from car import CARv1Writer
from file_types import BinaryFile

if __name__ == "__main__":
    with open("sample.html", "rb") as f:
        b = BinaryFile(f)
        c = CARv1Writer(b, "test.car")
        c.to_flat_dag()
