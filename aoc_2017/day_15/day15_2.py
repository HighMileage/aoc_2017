#!/usr/bin/env python3
import sys

def main(limit):
    a = 703
    b = 516

    all_as = []
    all_bs = []

    while not (len(all_as) >= limit and len(all_bs) >= limit):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647

        if a % 4 == 0: all_as.append(a)
        if b % 8 == 0: all_bs.append(b)

    count = 0
    print(
        'Done gathering matches. A matches: {} B matches: {}'.format(len(all_as), len(all_bs))
    )
    for a, b in zip(all_as, all_bs):
        if bin(a)[-16:] == bin(b)[-16:]: count += 1

    print('Total match count is {}'.format(count))


if __name__ == '__main__':
    limit = int(sys.argv[1])
    main(limit)
