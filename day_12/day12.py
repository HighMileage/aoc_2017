#!/usr/bin/env python3
import sys

def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        elements = [tuple(int(elem.strip()) for elem in (line.replace(' <-> ', ', ').split(','))) for line in input_file]
        nodes = [(elem[0], elem[1:]) for elem in elements]
    return nodes


def get_match_group(nodes, seed):
    i = 0
    while i < 20:
        for idx, value in enumerate(nodes):
            node, children = value
            # if node in seed:
            if seed.intersection([node]) or seed.intersection([children]):
                seed.add(node)
                seed.update(children)
        print('here goes {}'.format(i))
        i += 1
    return seed

def main(input_file):

    nodes = parse_file(input_file)
    zero_group = get_match_group(nodes, set([0]))

    print(len(set(zero_group)))
    print(zero_group)
    # import pdb; pdb.set_trace()


if __name__ == '__main__':
    target = sys.argv[1]
    main(target)
