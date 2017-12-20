#!/usr/bin/env python3
import sys
import re

def parse_file(input_file):
    """
    Break input file up into array of particles
    """

    p = re.compile('<([0-9,-]+)>')
    with open(input_file, 'r') as input_file:
        particles = []
        for idx, line in enumerate(input_file):
            particle = []
            particle.append('p_{}'.format(idx))
            for element in p.findall(line):
                measures = tuple(int(number) for number in element.split(","))
                particle.append(measures)
            particles.append(particle)
    return particles


def main(input_file, ticks):
    particles = parse_file(input_file)
    particles.sort(key=lambda x: manhattan_distance(x[1]))
    for moment in range(0, ticks):
        for idx, particle in enumerate(particles):
            name, pos, vel, accel = particle
            particles[idx][1] = tuple(sum(coordinates) for coordinates in zip(pos, vel))
            particles[idx][2] = tuple(sum(coordinates) for coordinates in zip(particle[2], particle[3]))
        particles.sort(key=lambda x: manhattan_distance(x[1]))
    print('After {} ticks, particle {} appears to be closest to zero'.format(ticks, particles[0][0]))


def manhattan_distance(coordinates):
    """
    Sum of all distances from zero
    """
    x, y, z = coordinates
    return abs(x) + abs(y) + abs(z)

if __name__ == '__main__':
    input_file = sys.argv[1]
    ticks = int(sys.argv[2])
    main(input_file, ticks)
