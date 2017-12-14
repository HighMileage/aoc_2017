#!/usr/bin/env python3
import sys
from collections import defaultdict

def parse_file(input_file):
    output = []
    with open(input_file, 'r') as input_file:
        directions = [direction.strip() for direction in input_file.read().split(',')]
        process_directions(directions)

def process_directions(directions):
        nw_se_count = directions.count('nw') - directions.count('se')
        ne_sw_count = directions.count('ne') - directions.count('sw')
        print('Total vertical movement is {}'.format(directions.count('n') - directions.count('s')))
        print('Move {} {}'.format('NW' if nw_se_count > 0 else 'SE', abs(nw_se_count)))
        print('Move {} {}'.format('NE' if nw_se_count > 0 else 'SW', abs(ne_sw_count)))
        total = sum([
            abs(directions.count('n') - directions.count('s')),
            # abs(directions.count('ne') - directions.count('sw')),
            abs(directions.count('nw') - directions.count('se')),
        ])
        print('Total distance away is {}'.format(total))
        # print('{} of N'.format(directions.count('n')))
        # print('{} of S'.format(directions.count('s')))
        # print('{} of SW'.format(directions.count('sw')))
        # print('{} of SE'.format(directions.count('se')))
        # print('{} of NW'.format(directions.count('nw')))
        # print('{} of NE'.format(directions.count('ne')))


def main(input_file):
    parse_file(input_file)


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
