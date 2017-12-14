#!/usr/bin/env python3
import re
import sys

def process_line(line):
    p = re.compile('\(([0-9]+)\)')

    name = line.split('->')[0].split()[0]
    weight = int(p.search(line).group(1))
    children = [i.strip() for i in line.split('->')[1].split(',')] if len(line.split('->')) > 1 else None

    return (name, weight, children)


def main(input_file):
    with open(input_file, 'r') as input_file:
        nodes = [process_line(row) for row in input_file.read().split('\n')[:-1]]

    network = Network()
    for hub in nodes:
        network.add_node(hub)

    for node in network.nodes:
        name, value, children = node
        if children:
            unique_values = set([network.node_weight(child) for child in children])
            if len(unique_values) != 1:
                # import pdb; pdb.set_trace()
                print(name)
                print('My parent is {}'.format(network.parent(name))
                print(unique_values)
                print(children)


    hubs = None
    while True:
        singletons = list(filter(lambda node: not node[2], hubs or nodes))
        if len(singletons) == 0:
            break
        hubs = list(filter(lambda node: node[2], hubs or nodes))

        for idx, node in enumerate(hubs):
            target, target_weight, children = node
            for singleton, weight, _ in singletons:
                if singleton in children:
                    node[2][children.index(singleton)] = (singleton, weight)
                # if condensable(node):
                #     hubs[idx] = (target, target_weight + sum(children), None)


class Network(object):
    def __init__(self):
        self.nodes = []

    def unique_nodes(self):
        return [node[0] for node in self.nodes]

    def add_node(self, node):
        name, value, children = node
        self.nodes.append((name, value, children))

    def parent(self, node_name):
        for node in self.nodes:
            name, value, children = node
            if children and node_name in children:
                return node

    def node_weight(self, node_name):
        name, weight, children = self.nodes[self.unique_nodes().index(node_name)]

        if not children:
            total = weight
        else:
            if all(isinstance(child, tuple) for child in children):
                total = weight + sum([child[1] for child in children])
            else:
                total = weight + sum([child[1] for child in children if isinstance(child, tuple)])
                for child in children:
                    if not isinstance(child, tuple):
                        total += self.node_weight(child)
        return total


# def node_weight(node, hubs):
#     name, weight, children = node
#     if all(isinstance(child, tuple) for child in children):
#         return weight + sum([child[1] for child in children])
#     else:
#         try:
#             hubbers = [hub[0] for hub in hubs]
#             partial = sum([child[1] for child in children if isinstance(child, tuple)])
#             for child in children:
#                 if not isinstance(child, tuple):
#                     partial += node_weight(hubs[hubbers.index(child)], hubs)
#             return partial
#             # return partial + sum([node_weight(hubs[hubbers.index(child)], hubs) for child in children])
#         except Exception as e:
#             import pdb; pdb.set_trace()

def condensable(node):
    if all(isinstance(disk, int) for disk in node[2]) and len(set(node[2])) == 1:
        return True
    # elif all(isinstance(disk, int) for disk in node[2]):
    #     print('Unbalanced disks at {}; disk values {}'.format(node[0], node[2]))

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
