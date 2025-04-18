import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def __str__(self):
        return f"UDP Header: {self.src_port}, {self.dst_port}, {self.length}, {self.checksum}"

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)

def unpack_Udphdr(data):
    return struct.unpack('!HHHH', data[:8])

def getSrcPort(unpacked_data):
    return unpacked_data[0]

def getDstPort(unpacked_data):
    return unpacked_data[1]

def getLength(unpacked_data):
    return unpacked_data[2]

def getChecksum(unpacked_data):
    return unpacked_data[3]

udp_header = Udphdr(5555, 80, 1000, 65535)

packed_data = udp_header.pack_Udphdr()
print(binascii.b2a_hex(packed_data))
unpacked_data = unpack_Udphdr(packed_data)
print(unpacked_data)
print(f"Source Port: {getSrcPort(unpacked_data)} Destination Port: {getDstPort(unpacked_data)} Length: {getLength(unpacked_data)} Checksum: {getChecksum(unpacked_data)}")