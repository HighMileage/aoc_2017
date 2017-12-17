#!/usr/bin/env python3
import sys


def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        directions = [direction.strip() for direction in input_file.read().split(',')]
    return directions


def main(input_file):

if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
