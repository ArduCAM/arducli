from smbus2 import SMBus, i2c_msg


class I2CDevice(object):
    def __init__(self, bus_num) -> None:
        self.bus_num = bus_num
        self.bus = SMBus(self.bus_num)
    
    def write_16_8(self, chip_address, register, value):
        msg = i2c_msg.write(chip_address, [(register & 0xFF00) >> 8, register & 0xFF, value & 0xFF])
        self.bus.i2c_rdwr(msg)

    def read_16_8(self, chip_address, register):
        msg_write = i2c_msg.write(chip_address & 0xFF, [(register & 0xFF00) >> 8, register & 0xFF])
        msg_read = i2c_msg.read(chip_address & 0xFF, 1)

        self.bus.i2c_rdwr(msg_write, msg_read)
        # print(msg_read.len)
        return int.from_bytes(msg_read.buf[0], "big")
    
    def write_16_16(self, chip_address, register, value):
        msg = i2c_msg.write(chip_address, [
            (register & 0xFF00) >> 8, register & 0xFF,
            (value & 0xFF00) >> 8, value & 0xFF
        ])
        self.bus.i2c_rdwr(msg)

    def read_16_16(self, chip_address, register):
        msg_write = i2c_msg.write(chip_address & 0xFF, [(register & 0xFF00) >> 8, register & 0xFF])
        msg_read = i2c_msg.read(chip_address & 0xFF, 2)

        self.bus.i2c_rdwr(msg_write, msg_read)
        # print(msg_read.len)
        return int.from_bytes(msg_read.buf[:2], "big")

    def write_16_32(self, chip_address, register, value):
        msg = i2c_msg.write(chip_address, [
            (register & 0xFF00) >> 8, register & 0xFF,
            (value & 0xFF000000) >> 24, (value & 0x00FF0000) >> 16,
            (value & 0x0000FF00) >> 8, (value & 0x000000FF) >> 0
        ])
        self.bus.i2c_rdwr(msg)

    def read_16_32(self, chip_address, register):
        msg_write = i2c_msg.write(chip_address & 0xFF, [(register & 0xFF00) >> 8, register & 0xFF])
        msg_read = i2c_msg.read(chip_address & 0xFF, 4)

        self.bus.i2c_rdwr(msg_write, msg_read)
        # print(msg_read.len)
        return int.from_bytes(msg_read.buf[:4], "big")
    
    def read_16_X(self, chip_address, register, len):
        msg_write = i2c_msg.write(chip_address & 0xFF, [(register & 0xFF00) >> 8, register & 0xFF])
        msg_read = i2c_msg.read(chip_address & 0xFF, len)

        self.bus.i2c_rdwr(msg_write, msg_read)
        # print(msg_read.len)
        return msg_read.buf

    def close(self):
        self.bus.close()

'''

with SMBus(10) as bus:
    # Write a single byte to address 80
    msg = i2c_msg.write(0x1a, [0x00, 0x16])
    bus.i2c_rdwr(msg)
    # Read 2 bytes from address 80
    msg = i2c_msg.read(0x1a, 2)
    bus.i2c_rdwr(msg)
    
    """
    # Write a single byte to address 80
    msg = i2c_msg.write(80, [65])
    bus.i2c_rdwr(msg)
    
    # Write some bytes to address 80
    msg = i2c_msg.write(80, [65, 66, 67, 68])
    bus.i2c_rdwr(msg)
    """
'''
    
    
