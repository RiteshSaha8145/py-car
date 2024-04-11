import dag_cbor
from protobufs import PBNode
from multiformats import CID


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
        while root_block:
            try:
                cid = root_block[: len(bytes(r))]
                block = root_block[len(bytes(r)) :]
                pbnode = PBNode()
                print(CID.decode(cid))
                pbnode.ParseFromString(block)
                root_size = read_varint(f)
                # print(pbnode)
            except Exception as e:
                print(e)
                continue
            finally:
                root_block = f.read(root_size)
