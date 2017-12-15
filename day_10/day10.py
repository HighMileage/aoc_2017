#!/usr/bin/env python3
import sys
import re
from collections import deque
import itertools

def main(input_file):
    with open(input_file, 'rt') as input_file:
        lengths = [int(length) for length in input_file.read().split(',')]
        print('Your hash is: {}'.format(process(lengths)))


def process(lengths):
    numbers = deque(range(0, 256))
    # numbers = deque(range(0, 5))
    position = 0
    skip = 0
    index = 0

    while skip < len(lengths):
        for length in lengths:
            orig_pos = position
            numbers.rotate(-orig_pos)

            front = deque(itertools.islice(numbers, 0, length))
            front.reverse()
            back = deque(itertools.islice(numbers, length, len(numbers)))
            numbers = front + back

            numbers.rotate(orig_pos)
            position += length + skip
            print(position)
            skip += 1

    return numbers[0] * numbers[1]


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
