#!/usr/bin/env python
import sys

def main(target_file):
    with open(target_file, 'r') as input_file:
        steps = [int(step) for step in input_file.read().split('\n')[:-1]]
    maze_length = len(steps)
    print('There are {} steps in this maze'.format(len(steps)))

    count = 0
    position = 0
    while True:
        jump = steps[position]
        print('Position has a jump value of {}'.format(jump))
        steps[position] = jump + 1
        print('Position updated with a jump value of {}'.format(steps[position]))
        position += jump
        count += 1
        if position > maze_length - 1 or position < 0:
            print('Exited maze after {} steps'.format(count))
            break


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
