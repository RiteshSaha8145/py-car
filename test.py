from car import CARv1Writer
from file_types import BinaryFile

if __name__ == "__main__":
    with open("sample.html", "rb") as f:
        c = CARv1Writer(BinaryFile(bufferedReader=f, chunkSize=1024), "test.car")
        print(c._get_root_cid)
        for _, cid in c._get_root_cid(max_children=5):
            print(cid)
