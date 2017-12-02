import struct
import nfc

service_code = 0x090f
num_blocks = 20

suica_history = []

def connected(tag):
    print tag


    sc = nfc.tag.tt3.ServiceCode(service_code >> 6, service_code & 0x3f)
    for i in range(num_blocks):
        bc = nfc.tag.tt3.BlockCode(i, service = 0)
        data = tag.read_without_encryption([sc], [bc])

        suica_hitory = suica_history.append(data)

        row_be = struct.unpack('>2B2H4BH4B', data)
        print(row_be)
        row_le = struct.unpack('<2B2H4BH4B', data)
        print(row_le[8])

if __name__ == "__main__":
    clf = nfc.ContactlessFrontend('usb')
    print clf
    clf.connect(rdwr={'on-connect': connected})

    print(suica_history)
