#!/usr/bin/env python3
from collections import deque
import sys

DANCE_STRING='abcdefghijklmnop'
# DANCE_STRING='abcde'

def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        directions = [direction.strip() for direction in input_file.read().split(',')]
    return directions


def main(input_file):
    directions = parse_file(input_file)
    the_string = deque(list(DANCE_STRING))
    for direction in directions:
        if direction[0] == 's':
            direction = direction.replace('s','')
            spin = int(direction)
            the_string.rotate(spin)

        elif direction[0] == 'x':
            replacer, replacee = [the_string[int(direction)] for direction in direction[1:].split('/')]
            for idx, letter in enumerate(the_string):
                if letter == replacer: the_string[idx] = replacee
                if letter == replacee: the_string[idx] = replacer

        elif direction[0] == 'p':
            replacer, replacee = direction[1:].split('/')
            for idx, letter in enumerate(the_string):
                if letter == replacer: the_string[idx] = replacee
                if letter == replacee: the_string[idx] = replacer
    print('This string your look for appears to be \'{}\''.format(''.join(the_string)))


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
