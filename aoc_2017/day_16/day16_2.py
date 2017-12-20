#!/usr/bin/env python3
from collections import deque
import sys

DANCE_STRING=list('abcdefghijklmnop')
DANCE_STRING_TEST=list('abcde')

def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        directions = [direction.strip() for direction in input_file.read().split(',')]
    return cleaned_directions(directions)

def cleaned_directions(directions):
    """
    Created cleaned tuples for each dance move
    """
    directions = deque(directions)
    for idx, direction in enumerate(directions):
        if direction[0] == 's':
            directions[idx] = ('s', int(direction[1:]))
        elif direction[0] == 'x':
            value_1, value_2 = (int(part) for part in direction[1:].split('/'))
            directions[idx] = ('x', value_1, value_2)
        elif direction[0] == 'p':
            value_1, value_2 = (part for part in direction[1:].split('/'))
            directions[idx] = ('p', value_1, value_2)
    return directions


def main(input_file, iterations):
    directions = parse_file(input_file)
    the_string = deque(DANCE_STRING_TEST) if 'test' in input_file else deque(DANCE_STRING)
    partners = [direction for direction in directions if direction[0] == 'p']
    spin_exchanges = [direction for direction in directions if direction[0] in ('x', 's')]
    signature = None
    seen_values = []

    for iteration in range(0, iterations):
        for sub in partners:
            _, value_1, value_2 = sub
            replacer = (the_string.index(value_1), value_1)
            replacee = (the_string.index(value_2), value_2)
            the_string[replacee[0]] = replacer[1]
            the_string[replacer[0]] = replacee[1]

        if signature:
            the_string = [the_string[index] for index in signature]
            if the_string == list(DANCE_STRING):
                current_iter = iteration + 1
                equivalent = iterations % current_iter
                print('Looks like the string is cycling: Found a duplicate at iteration {}'.format(current_iter))
                print('{} iterations will be the same as {}'.format(equivalent, iterations))
                print('After {} iterations the string would be {}'.format(iterations,
                    seen_values[equivalent - 1]))
                break
        else:
            starting_value = [value for value in the_string]
            for direction in spin_exchanges:
                if len(direction) == 2:
                    _, value = direction
                    the_string.rotate(value)
                if len(direction) == 3:
                    _, value_1, value_2 = direction
                    replacer = (value_1, the_string[value_1])
                    replacee = (value_2, the_string[value_2])
                    the_string[replacee[0]] = replacer[1]
                    the_string[replacer[0]] = replacee[1]
            signature = [starting_value.index(letter) for letter in the_string]
        seen_values.append(''.join(the_string))


if __name__ == '__main__':
    input_file = sys.argv[1]
    iterations = int(sys.argv[2])
    main(input_file, iterations)
