#!/usr/bin/env python3
import sys

def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        parameters = [[int(line.split(':')[0].strip()), int(line.split(':')[1].strip())] for line in input_file]
    return parameters


def no_collisions(parameters, offset):
        return 0 not in ((layer + offset) % ((depth - 1) * 2) for layer, depth in parameters)


def main(input_file):
    parameters = parse_file(input_file)
    offset = 0
    while True:
        if no_collisions(parameters, offset):
            print('No collisions at {}'.format(offset))
            break
        offset += 1

if __name__ == '__main__':
    target = sys.argv[1]
    main(target)
