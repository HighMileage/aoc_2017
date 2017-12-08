#!/usr/bin/env python3
import re
import sys

def main(input_file):
    p = re.compile('\(([0-9]+)\)')
    with open(input_file, 'r') as input_file:
        nodes = [(row.split('->')[0].strip().split()[0], int(p.search(row).group(1)),
            [i.strip() for i in row.split('->')[1].split(',')] if len(row.split('->')) > 1 else None) for row in input_file.read().split('\n')[:-1]]

    while True:
        solo_dolos = []
        for idx, pair in enumerate(nodes):
            if not pair[2]:
                solo_dolos.append(pair)

        ends = list(filter(lambda node: not node[2], nodes))
        hubs = list(filter(lambda node: node[2], nodes))

        import pdb; pdb.set_trace()

        # print(len(pairs))
        for idx, pair in enumerate(pairs):
            for solo in solo_dolos:
                if solo[0] in pair[2]:
                    index = pair[2].index(solo[0])
                    pair[2][index] = solo[1]
                if ready_to_condense(pair):
                    # import pdb; pdb.set_trace()
                    pairs[idx] = (pair[0], pair[1] + sum(pair[2]), None)
        # for i in pairs:
        #     print(i)

def ready_to_condense(node):
    if all(isinstance(disk, int) for disk in node[2]) and len(set(node[2])) == 1:
        if node[0] == 'fabacam':
            print(node)
        return True
    # elif all(isinstance(disk, int) for disk in node[2]):
        # print('Unbalanced disks at {} disk values {}'.format(node[0], node[2]))

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
