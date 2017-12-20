#!/usr/bin/env python3
import sys
from collections import defaultdict


def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        matrix = [tuple(line[:-1]) for line in input_file]
    return matrix


def get_neighbors(coordinates):
    x, y = coordinates
    neighbors = [
            (x, y - 1),
            (x, y + 1),
            (x + 1, y),
            (x - 1, y),
    ]

    return neighbors


def main(input_file):
    matrix = parse_file(input_file)
    current_coordinates = (matrix[0].index('|'), 0)
    change = (0, 1)
    letters = []
    previous = None

    while True:
        x, y = current_coordinates
        # print('Currently at {}'.format(current_coordinates))
        value = matrix[y][x]
        if value not in ('+', ' ', '-', '|', ''):
            letters.append(value)
        elif value == ' ':
            break
        print(value)

        if value == '+':
            # next_coordinate = [neighbor for neighbor in get_neighbors((x, y)) if
            #         (matrix[neighbor[1]][neighbor[0]] not in (' ') and neighbor != previous)]

            next_coordinate = []
            for neighbor in get_neighbors((x, y)):
                try:
                    if matrix[neighbor[1]][neighbor[0]] not in (' ') and neighbor != previous:
                        next_coordinate.append(neighbor)
                    # if len(next_coordinate) > 1:
                    #     values = [matrix[neighbor[1]][neighbor[0]] for neighbor in next_coordinate]
                    #     import pdb; pdb.set_trace()
                except IndexError:
                    continue

            new_x, new_y = next_coordinate[0]
            delta_x = new_x - x
            delta_y = new_y - y
            change = (delta_x, delta_y)

        previous = current_coordinates
        current_coordinates = tuple(sum(coordinates) for coordinates in zip(current_coordinates, change))
    print('The letters you encountered were {}'.format(''.join(letters)))


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
