#!/usr/bin/env python
import itertools

def main():
    with open('day2.input', 'r') as input_file:
        contents = input_file.read()
        rows = [[int(cell) for cell in row.split()] for row in contents.split('\n')[:-1]]
        checksum = get_checksum(rows)
    print(checksum)

def get_checksum(rows):
    # Part 1 original solution
    # return sum([max(row) - min(row) for row in rows])
    final = []
    for row in rows:
        print("Processing row {}".format(row))
        for pair in itertools.permutations(row, 2):
            if pair[0] % pair[1] == 0:
                print("Found {} and {}".format(pair[0], pair[1]))
                final.append(int(pair[0]/pair[1]))

    return sum(final)

if __name__ == '__main__':
    main()
