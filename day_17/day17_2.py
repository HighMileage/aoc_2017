#!/usr/bin/env python3
import sys

JUMP=369

def main(steps):
    index = 0
    final = None
    for step in range(1, steps + 1):
        index = (index + 1 + JUMP) % step
        if index == 0:
            final = step
            # print('Got a new index {} at iteration {}'.format(index, step))
    print('The value after zero is {}'.format(final))

if __name__ == '__main__':
    steps = int(sys.argv[1])
    main(steps)
