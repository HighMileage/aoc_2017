#!/usr/bin/env python
import math
import sys

def main(number):
    ceiling = sqrt_ceiling(number)
    print("Ceiling is {}".format(ceiling))
    floor = ceiling - 2
    jumpsize = ceiling - 1
    print('Jump size is {}'.format(jumpsize))

    check = floor**2 + jumpsize
    print('Checking values less than or equal to:')
    while check <= ceiling**2:
        distance = None
        middle_value = int(check - (jumpsize/2))
        max_distance = ceiling - 1
        middle_distance = int(max_distance / 2)

        print('   {}...'.format(check))
        if number == check:
            distance = max_distance
        elif number < check:
            diff = abs(middle_value - number)
            distance = middle_distance + diff

        if distance:
            print("Distance away is {}".format(distance))
            break

        check += jumpsize


def sqrt_ceiling(number):
    """
    Returns the odd integer whose square is greater than and closest to input number
    """
    if math.ceil(math.sqrt(number)) % 2 == 0:
        return (math.ceil(math.sqrt(number)) + 1)
    else:
        return math.ceil(math.sqrt(number))


if __name__ == '__main__':
    arg = int(sys.argv[1])
    main(arg)
