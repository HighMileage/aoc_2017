#!/usr/bin/env python3
import sys

def parse_file(input_file):
    output = []
    with open(input_file, 'r') as input_file:
        directions = [direction.strip() for direction in input_file.read().split(',')]
        process_directions(directions)

def process_directions(directions):
        nw_se_count = 0
        ne_sw_count = 0
        vertical_count = 0
        maxes = []
        for direction in directions:
            if direction == 'n':
                vertical_count += 1
            elif direction == 's':
                vertical_count -= 1
            elif direction == 'nw':
                nw_se_count += 1
            elif direction == 'se':
                nw_se_count -= 1
            elif direction == 'nw':
                nw_se_count += 1
            elif direction == 'se':
                nw_se_count -= 1
            maxes.append(sum([
                abs(vertical_count),
                abs(nw_se_count),
                abs(ne_sw_count),
            ]))
        print(max(maxes))


def main(input_file):
    parse_file(input_file)


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
