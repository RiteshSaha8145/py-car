from pycar.car import folder_to_dag, CARv1Writer


if __name__ == "__main__":
    with CARv1Writer(
        None,
        "test4.car",
        unixfs=True,
        max_children=11,
    ) as c:
        cid = folder_to_dag(car_writer=c, folder_path="./car", chunk_size=242144)
