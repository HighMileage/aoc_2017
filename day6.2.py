#!/usr/bin/env python3
import sys
import copy
import time

def main(input_file):
    with open(input_file, 'r') as input_file:
        banks = [int(bank) for bank in input_file.read().split()]

    states = []
    count = 0
    partitions = len(banks)
    print('Initial banks state => {}'.format(banks))
    while True:
        reserve = max(banks)
        target = banks.index(reserve)
        banks[target] = 0
        index = target + 1
        while reserve > 0:
            banks[index % partitions] += 1
            reserve -= 1
            index += 1

        count += 1
        print('{} step{} complete. Banks state => {}'.format(count, 's' if count > 1 else '', banks))
        if banks in states:
            loop_size = count - states.index(banks) - 1
            print('Loop size is {}'.format(loop_size))
            break
        else:
            states.append(copy.deepcopy(banks))
        # print(states)

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
