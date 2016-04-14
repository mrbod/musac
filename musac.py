#!/usr/bin/env python
import sys
import math
import random
import struct
import subprocess

encoder = struct.Struct('<l')

def foo():
    freqs = [330.0 * 2**(x / 12.0) for x in [0, 2, 4, 5, 7, 8, 10, 12]]
    while True:
        f = random.choice(freqs)
        i = 0.0
        while i < 1.0:
            x = int(20.0 * math.sin(math.pi * f * i))
            yield encoder.pack(x)
            i += 0.0001

for x in foo():
    print(x)
