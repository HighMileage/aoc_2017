#!/usr/bin/env python3
import sys
from collections import defaultdict

OPERATIONS = {
        '>=': '__ge__',
        '<=': '__le__',
        '>': '__gt__',
        '<': '__lt__',
        '==': '__eq__',
        '!=': '__ne__',
}

def parse_file(input_file):
    output = []
    with open(input_file, 'r') as instructions:
        for row in instructions.read().split('\n')[:-1]:
            target, sign, value, _, statement = row.split(None, 4)
            output.append(
                    (
                    target,
                    -1*int(value) if sign == 'dec' else int(value),
                    statement
                    )
            )
    return output


def main(input_file):
    registers = defaultdict(int)
    all_observations = []
    instructions = parse_file(input_file)

    for target, value, statement in instructions:
        check = statement.split()[0]
        op = statement.split()[1]
        criteria = int(statement.split()[2])

        if getattr(registers[check], OPERATIONS[op])(criteria):
            registers[target] += value

        all_observations.append(registers[target])

    print('Largest final register: {}'.format(max([v for k,v in registers.items()])))
    print('Largest witnessed register: {}'.format(max(all_observations)))


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
