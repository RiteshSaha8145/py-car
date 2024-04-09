from car import CARv1Writer
from file_types import BinaryFile

if __name__ == "__main__":
    with open("dna.txt", "rb") as f:
        with CARv1Writer(
            BinaryFile(bufferedReader=f, chunkSize=1, metadata={"name": "dna.txt"}),
            "test.car",
            max_children=11,
        ) as c:
            c.get_car()
