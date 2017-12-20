#!/usr/bin/env python3
import sys
import copy
import time
import re

def main(input_file):
    p = re.compile('\(([0-9]+)\)')
    with open(input_file, 'r') as input_file:
        pairs = [(row.split('->')[0].strip().split()[0], int(p.search(row).group(1)),
            [i.strip() for i in row.split('->')[1].split(',')] if len(row.split('->')) > 1 else None) for row in input_file.read().split('\n')[:-1]]

    print(pairs[1])
    roots = []
    branches = []
    for pair in pairs:
        if pair[2]:
            roots.append(pair[0])
            branches += pair[2]

    uniques = set(branches)

    for root in roots:
        if root not in branches:
            print('Looks like the lone wolf here is {}'.format(root))

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
