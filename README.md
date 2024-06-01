# pycar

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

`pycar` is a Python package designed to facilitate the conversion of files and folders into Content Addressable Archive (CARv1) files. The CAR format (Content Addressable aRchives) can be used to store content addressable objects in the form of IPLD block data as a sequence of bytes, typically in a file with a .car filename extension.

The CAR format serves as a serialized representation of any IPLD DAG (graph) as the concatenation of its blocks, plus a header that describes the graphs in the file via root CIDs. While the requirement for the blocks in a CAR to form coherent DAGs is not strict, the CAR format may also be used to store arbitrary IPLD blocks.

In addition to the binary block data, storage overhead for the CAR format includes a header block encoded as DAG-CBOR containing the format version and an array of root CIDs, along with a CID for each block preceding its binary data. Moreover, a compressed integer prefixes each block (including the header block), indicating the total length of that block, including the length of the encoded CID.

The `pycar` package provides a simple yet powerful API for creating CARv1 files from local file systems. Users can choose the chunk size and the number of children per node to customize the conversion process according to their requirements.

For more information about the CARv1 specification, please refer to [CARv1 Specification](https://ipld.io/specs/codecs/car/).



## Installation
```bash
pip install pycar
```

## Usage

### Converting Folders to CARv1 Files
```python
from pycar import CARv1Writer, folder_to_dag

with CARv1Writer(file=None, name="example.car") as car_writer:
    cid = folder_to_dag(car_writer, "/path/to/folder", chunk_size=262144)
    print("CARv1 CID:", cid)
```

### Converting Files to CARv1 Files
```python
from pycar.car import CARv1Writer
from pycar.file_types import BinaryFile

with open("dummy_file_path", "rb") as f:
    with CARv1Writer(
        BinaryFile(bufferedReader=f, chunkSize=1, metadata={"name": "dummyfile"}),
            "dummyfile.car",
            unixfs=True,
            max_children=1024,
        ) as car:
            cid = car.get_car()
    print("CARv1 CID:", cid)
```
