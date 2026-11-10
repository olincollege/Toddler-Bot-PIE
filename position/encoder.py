from smbus2 import SMBus
import time

with SMBus(0) as bus:
    while True:
        # Read a block of 16 bytes from address 80, offset 0
        block = bus.read_i2c_block_data(80, 0, 16)
        print(block)
        time.sleep(1)
    