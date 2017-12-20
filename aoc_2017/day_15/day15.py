#!/usr/bin/env python3

def main():
    a = 703
    b = 516

    count = 0
    for i in range(0, 40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647

        if bin(a)[-16:] == bin(b)[-16:]: count += 1

    print('Total is {}'.format(count))


if __name__ == '__main__':
    main()
