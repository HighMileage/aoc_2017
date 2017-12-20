#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        directions = [[int(line.split(':')[0].strip()), int(line.split(':')[1].strip())] for line in input_file]
    return directions

def run_firewall(directions):
    ticks = len(directions)
    fw = Firewall(directions)
    fw.tick()
    print('Total penalty is {}'.format(fw.penalty))

class Firewall(object):
    def __init__(self, layer_spans):
        self.layers = defaultdict(lambda: None)
        for layer, span in layer_spans:
            self.layers[layer] = [deque([1] + [0]*int(span - 1)), 1]
        self.max_layers = max(layer for layer, span in layer_spans) + 1
        self.penalty = 0

    def tick(self):
        for current_layer in range(0, self.max_layers):
            for layer in list(self.layers.keys()):
                the_range, direction = self.layers[layer]
                print(the_range)
                # if layer == 0:
                #     print('Picosecond: {}'.format(current_layer))
                if the_range[0] == 1 and current_layer == layer:
                    print('Getting caught on picosecond {} in layer {}'.format(current_layer,
                        layer))
                    self.penalty += len(the_range) * layer
                the_range.rotate(direction)
                if the_range[-1] == 1 or the_range[0] == 1:
                    self.layers[layer][1] = direction * -1
            print('\n')


def main(input_file):
    directions = parse_file(input_file)
    run_firewall(directions)

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
