import dag_cbor
from protobufs import PBNode


def read_varint(f):
    result = 0
    shift = 0
    while True:
        byte = f.read(1)[0]
        result |= (byte & 0x7F) << shift
        shift += 7
        if not (byte & 0x80):
            break
    return result


def read_varint1(f):
    varint_bytes = bytearray()
    while True:
        byte = f.read(1)
        varint_bytes.extend(byte)
        if not (byte[0] & 0x80):
            break
    return bytes(varint_bytes)


if __name__ == "__main__":
    with open("test.car", "rb") as f:
        header_size = read_varint(f)
        header_bytes = f.read(header_size)
        header = dag_cbor.decode(header_bytes)

        r = header["roots"][0]

        print(r)

        root_size = read_varint(f)
        root_block = f.read(root_size)
        print(root_size)

        root_node = PBNode()
        root_node.ParseFromString(root_block)

        # print(root_node)
