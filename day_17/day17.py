#!/usr/bin/env python3
# To run:
# ./day17_2.py 50000000
from collections import deque
import sys

JUMP=369

def main(steps):
    buffy = [0]
    index = 0
    for step in range(1, steps + 1):
        index += 1
        buffy = buffy[:index] + [step] + buffy[index:]
        index = (index + JUMP) % len(buffy)
    print(buffy[buffy.index(2017) + 1])

if __name__ == '__main__':
    steps = int(sys.argv[1])
    main(steps)
