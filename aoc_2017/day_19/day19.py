#!/usr/bin/env python3
import sys


def parse_file(input_file):
    """
    Break input file up into a list of tuples
    """
    with open(input_file, 'r') as input_file:
        matrix = [tuple(line[:-1]) for line in input_file]
    return matrix


def get_neighbors(coordinates):
    """
    Returns an array of all coordinates adjacent but not diagonal to the coordinates
    """
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
    count = 0

    while True:
        x, y = current_coordinates
        value = matrix[y][x]

        if value not in ('+', ' ', '-', '|', ''):
            letters.append(value)

        elif value == ' ':
            break

        elif value == '+':
            for neighbor in get_neighbors((x, y)):
                try:
                    if matrix[neighbor[1]][neighbor[0]] not in (' ') and neighbor != previous:
                        next_coordinate = neighbor
                except IndexError:
                    continue

            change = (next_coordinate[0] - x, next_coordinate[1] - y)

        previous = current_coordinates
        current_coordinates = tuple(sum(coordinates) for coordinates in zip(current_coordinates, change))
        count += 1
    print('The letters you encountered were {} after {} steps--neato!'.format(''.join(letters), count))


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
