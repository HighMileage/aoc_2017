#!/usr/bin/env python
import math
import sys

class Matrix(object):
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.matrix = [[0 for col in range(self.x_max)] for row in range(y_max)]


    def update(self, coordinates, value):
        x = coordinates[0]
        y = coordinates[1]
        self.matrix[x][y] = value


    def neighbors(self, x, y):
        return  [
                    [x - 1, y + 1],
                    [x, y + 1],
                    [x + 1, y + 1],
                    [x - 1, y],
                    [x + 1, y],
                    [x - 1, y - 1],
                    [x, y - 1],
                    [x + 1, y - 1],
                ]


    def new_value(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]
        neighbors = self.neighbors(x, y)
        return sum(self.matrix[neighbor[0]][neighbor[1]] for neighbor in neighbors if
                abs(neighbor[0]) <=
                len(self.matrix[0]) - 1 and abs(neighbor[1]) <= len(self.matrix) - 1)


def build_spiral(x, y, step):
    m = Matrix(501, 501)
    m.update((x, y), 1)
    movements = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while True:
        if odd_perfect_square(step):
            jump = int(math.sqrt(step) + 1)
            positions = []
            for movement in movements:
                positions += [movement]*jump
            positions[0] = (1, 0)
        for position in positions:
            step += 1
            x += position[0]
            y += position[1]
            new_value = m.new_value((x,y))
            print('...{}'.format(new_value))
            m.update((x, y), new_value)
            if new_value > 289326:
                return new_value


def odd_perfect_square(number):
    return math.floor(math.sqrt(number))**2 == number and math.sqrt(number) % 2 != 0


def main():
    print('Found value {}'.format(build_spiral(250,250, 1)))

if __name__ == '__main__':
    main()
