from smbus2 import SMBus
import time
from numpy import pi
with SMBus(1) as bus:
    while True:
        # Read a block of 16 bytes from address 80, offset 0
        start = time.time()
        block = bus.read_i2c_block_data(8, 0, 4)
        block = bus.read_i2c_block_data(8, 0, 4)
        end = time.time()
        print(end - start)
        print((block[0]*255 + block[1] - 2400)*(2*pi)/2400, (block[2]*255 + block[3] - 2400)*(2*pi)/2400)
        time.sleep(1)
    