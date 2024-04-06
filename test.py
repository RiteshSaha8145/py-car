from car import CARv1Writer
from file_types import BinaryFile

if __name__ == "__main__":
    with open("requirements.txt", "rb") as f:
        c = CARv1Writer(BinaryFile(bufferedReader=f, chunkSize=1), "test2.car")
        c.get_car()
