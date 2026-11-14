from smbus2 import SMBus
import time

with SMBus(1) as bus:
    while True:
        # Read a block of 16 bytes from address 80, offset 0
        block = bus.read_i2c_block_data(8, 0, 4)
        block = bus.read_i2c_block_data(8, 0, 4)
        print(block)
        print(block[0]*block[1], block[2]*block[3])
        time.sleep(1)
    