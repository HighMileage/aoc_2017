#!/usr/bin/env python3
import sys
import re
from collections import deque
import itertools

FIXED_SUFFIX=[17, 31, 73, 47, 23]

def main(input_file):
    with open(input_file, 'rt') as input_file:
        lengths = input_file.read().split('\n')[:-1]
        for length in lengths:
            the_input = [i for i in length.encode('ascii')] + FIXED_SUFFIX

            knot_hash = process(the_input)
            print("The input '{}' produced a hash of {}".format(length, knot_hash))


def process(lengths):
    numbers = deque(range(0, 256))
    position = 0
    skip = 0
    index = 0

    while index <= 63:
        # print(position)
        # print('On round: {}'.format(index + 1))
        for length in lengths:
            orig_pos = position
            numbers.rotate(-orig_pos)

            inty = length
            front = deque(itertools.islice(numbers, 0, inty))
            front.reverse()
            back = deque(itertools.islice(numbers, inty, len(numbers)))
            numbers = front + back

            numbers.rotate(orig_pos)
            position += length + skip
            skip += 1
        index += 1

    dense = dense_hash(list(numbers))
    knot_hash = get_hex(dense)
    return knot_hash

def get_hex(dense):
    return ''.join([hex(element).replace('0x', '').rjust(2, '0') for element in dense])


def dense_hash(sparse_hash):
    chunks = [chunk for chunk in get_chunks(sparse_hash, 16)]
    dense_hash = []
    for chunk in chunks:
        previous = None
        for element in chunk:
            if not previous:
                previous = element
            else:
                previous = previous ^ element
        dense_hash.append(previous)
    return dense_hash


def get_chunks(input_list, size):
    for i in list(range(0, len(input_list), size)):
            yield input_list[i:i + size]


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
