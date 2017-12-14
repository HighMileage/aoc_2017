#!/usr/bin/env python3
import sys
import re

def main(input_file):
    with open(input_file, 'rt') as input_file:
        lines = input_file.read().split('\n')[:-1]
        for line in lines:
            process_line(line)


def process_line(line):
    cleaned = re.sub("(!!)", "", line)
    recleaned = re.sub("!.", "", cleaned)
    garbage_less = re.sub("<[^>]*>", "<>", recleaned)
    final = re.sub("<>,|,<[^>]*>|<>|", "", garbage_less)
    total = score_counter(final)
    two = garbage_length(recleaned)
    print('The score of this stream of data is {}'.format(total))
    print('Number of non-cancelled characters in the garbage is: {}'.format(two))

def garbage_length(input_string):
    p = re.compile('<[^>]*>')
    garbage = re.findall(p, input_string)
    return(sum([len(bag) - 2 for bag in garbage]))

def score_counter(input):
    depth = 0
    total = []
    for idx, value in enumerate(input):
        if value == '{':
            depth += 1
        if value == '}':
            total.append(depth)
            depth -= 1
    return sum(total)


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
