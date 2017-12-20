#!/usr/bin/env python3
import sys
import re
from collections import deque
import itertools

PREFIX='hwlqcszp'
# PREFIX='flqrgnkx'
FIXED_SUFFIX=[17, 31, 73, 47, 23]
HEX_TO_BINARY={
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
SAMPLE=[
    '110101001111011101101',
    '010101011110101010110',
    '000010101101111100010',
    '101011010011110110100',
    '011010000010111111100',
    '110010011111010111111',
    '010001001100000000011',
]

def main():
    total = 0
    grid = Matrix(128, 128)
    for row in range(0, 128):
        the_input = '{}-{}'.format(PREFIX, row)
        byte_input = [i for i in the_input.encode('ascii')] + FIXED_SUFFIX
        knot_hash = process(byte_input)
        binary = hex_to_binary(knot_hash)

        for x, value in enumerate(binary):
            grid.update((x, row), int(value))

        # import pdb; pdb.set_trace()
        total += binary.count('1')
        # output = regionize([list(row) for row in SAMPLE])
        # print(str(binary).replace('0',' '))
        # for i in output:
        #     print(i[1])
        # print("The input '{}' produced a hash of {} with binary of {}".format(the_input, knot_hash, binary))
    # import pdb; pdb.set_trace()
    for index, coordinate in enumerate(grid.coordinates()):
        index += 2
        grid.update_around(coordinate, index)
    final = set()
    for row in grid.matrix:
        final.update(row)
    # import pdb; pdb.set_trace()

    final.remove(0)
    print('Total unique groups are {}'.format(len(set(final))))
    print('Total number of squares used is {}'.format(total))


class Matrix(object):
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.matrix = [[0 for col in range(self.x_max)] for row in range(y_max)]


    def __str__(self):
        output = []
        for row in self.matrix:
            output.append(''.join([str(element) for element in row]))
        return '\n'.join(str(row) for row in output)


    def update(self, coordinates, value):
        x, y = coordinates
        self.matrix[y][x] = value


    def get(self, coordinates):
        x, y = coordinates
        if x < self.x_max and x >= 0 and y < self.y_max and y >= 0:
            value = self.matrix[y][x]
        else:
            value = None

        return value


    def neighbors(self, coordinates):
        x, y = coordinates
        return  (
                    (x, y + 1),
                    (x, y - 1),
                    (x - 1, y),
                    (x + 1, y),
                )


    def update_around(self, coordinates, update_value):
        """
        Updates any values around the coordinate that are populated
        """
        x, y = coordinates
        if self.get(coordinates) == 0:
            return
        elif self.get(coordinates) == 1:
            self.update(coordinates, update_value)
        updated = []
        neighbors = self.neighbors((x, y))
        for neighbor in neighbors:
            if self.get(neighbor) == 1:
                self.update(neighbor, update_value)
                updated.append(neighbor)

        return [] + [self.update_around(update, update_value) for update in updated]


    def coordinates(self):
        """
        Returns array of all coordinates in the grid
        """
        coordinates = []
        for x in range(0, self.x_max):
            for y in range(0, self.y_max):
                coordinates.append((x, y))
        return coordinates


def regionize(matrix):
    group = 0
    for y, row in enumerate(matrix):
        coded_row = []
        for x, cell in enumerate(row):
            new_value = '.'
            if y == 0:
                if cell == 1 and x-1 >= 0 and matrix[y][x-1] == 1:
                    new_value = matrix[y][x-1]
                elif cell == 1 and x-1 >= 0 and matrix[y][x-1] != 1:
                    new_value = group + 1
            else:
                if cell == 1 and matrix[y-1][x] == 1:
                    new_value = matrix[y-1][x]
                elif cell == 1 and x-1 >= 0 and matrix[y][x-1] == 1:
                    new_value = matrix[y][x-1]
                elif cell == 1:
                    new_value = group + 1

            # import pdb; pdb.set_trace()
            matrix[y][x] = [cell, new_value]
            group += 1
    return matrix


def hex_to_binary(hexadecimal):
    return ''.join(HEX_TO_BINARY[letter.upper()] for letter in hexadecimal)


def process(lengths):
    numbers = deque(range(0, 256))
    position = 0
    skip = 0
    index = 0

    while index <= 63:
        for length in lengths:
            orig_pos = position
            numbers.rotate(-orig_pos)

            inty = length
            front = deque(itertools.islice(numbers, 0, inty))
            front.reverse()
            back = deque(itertools.islice(numbers, inty, len(numbers)))
            numbers = front + back

            numbers.rotate(orig_pos)
            position += length + skip
            skip += 1
        index += 1

    dense = dense_hash(list(numbers))
    knot_hash = get_hex(dense)
    return knot_hash

def get_hex(dense):
    return ''.join([hex(element).replace('0x', '').rjust(2, '0') for element in dense])


def dense_hash(sparse_hash):
    chunks = [chunk for chunk in get_chunks(sparse_hash, 16)]
    dense_hash = []
    for chunk in chunks:
        previous = None
        for element in chunk:
            if not previous:
                previous = element
            else:
                previous = previous ^ element
        dense_hash.append(previous)
    return dense_hash


def get_chunks(input_list, size):
    for i in list(range(0, len(input_list), size)):
            yield input_list[i:i + size]

if __name__ == '__main__':
    main()
