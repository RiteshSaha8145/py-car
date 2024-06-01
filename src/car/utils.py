from os import walk, path
from file_types import BinaryFile
from multiformats import CID  # type: ignore
from protobufs import Data
from . import CARv1Writer


def folder_to_dag(
    car_writer: CARv1Writer, folder_path: str, chunk_size: int = 262144
) -> CID:
    def helper(folder_path):
        folder_node, folder_unixfs = car_writer._get_pbnode(
            dtype=Data.DataType.Directory
        )
        total_size = 0

        def add_link(cid, name, size):
            link = car_writer._get_pblink(cid=cid, name=name, size=size)
            folder_node.Links.extend([link])
            folder_unixfs.blocksizes.extend([size])

        try:
            for root, dirs, files in walk(folder_path):
                for file in files:
                    file_path = path.join(root, file)
                    with open(file_path, "rb") as bytestream:
                        car_writer.file = BinaryFile(
                            bufferedReader=bytestream,
                            chunkSize=chunk_size,
                            metadata={"name": file},
                        )
                        size, cid = car_writer._get_file_node()
                        add_link(cid=cid, name=file, size=size)
                        total_size += size
                for dir in dirs:
                    dir_path = path.join(root, dir)
                    size, cid = helper(dir_path)
                    add_link(cid=cid, name=dir, size=size)
                    total_size += size
                break
            _, directory_cid = car_writer._serialize_and_write_pbnode(
                pbnode=folder_node, unixfs=folder_unixfs, codec="dag-pb"
            )
            return (total_size, directory_cid)
        except FileNotFoundError:
            raise FileNotFoundError(f"Folder '{folder_path}' not found.")

    _, cid = helper(folder_path=folder_path)
    car_writer._write_header(cid=cid)
    return cid
