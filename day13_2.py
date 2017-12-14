#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        directions = [[int(line.split(':')[0].strip()), int(line.split(':')[1].strip())] for line in input_file]
    return directions


def run_firewall(directions, offset):
    for off in range(0, offset):
        if off % 100 == 0:
            print(off)
        fw = Firewall(directions)
        fw.tick(off)
        layers = fw.layers
        fw.run()
        if fw.penalty == 0:
            print('Total penalty is {} with an offset of {}'.format(fw.penalty, off))


class Firewall(object):
    def __init__(self, layer_spans):
        self.layers = defaultdict(lambda: None)
        for layer, span in layer_spans:
            self.layers[layer] = [deque([1] + [0]*int(span - 1)), 1]
        self.max_layers = max(layer for layer, span in layer_spans) + 1
        self.penalty = 0


    def tick(self, offset):
        if offset == 0: return
        # print('**** Handling offset {} ****'.format(offset))
        else:
            for picosecond in range(0, offset):
                # print('Picosecond: {}'.format(picosecond))
                for layer in list(self.layers.keys()):
                    the_range, direction = self.layers[layer]
                    the_range.rotate(direction)
                    if the_range[-1] == 1 or the_range[0] == 1:
                        self.layers[layer][1] = direction * -1
                    # print(self.layers[layer][0])


    def run(self):
        for picosecond in range(0, self.max_layers):
            for layer in list(self.layers.keys()):
                the_range, direction = self.layers[layer]
                # print(the_range)
                # import pdb; pdb.set_trace()
                if the_range[0] == 1 and picosecond == layer:
                    current_penalty = len(the_range) * layer
                    self.penalty += current_penalty if current_penalty != 0 else 1
                    return 5
                    # print('Getting caught on picosecond {} in layer {}'.format(picosecond,
                    #     layer))
                the_range.rotate(direction)
                if the_range[-1] == 1 or the_range[0] == 1:
                    self.layers[layer][1] = direction * -1
            # print('\n')


def main(input_file, offset):
    directions = parse_file(input_file)
    run_firewall(directions, offset)


if __name__ == '__main__':
    target = sys.argv[1]
    offset = int(sys.argv[2])
    main(target, offset)
