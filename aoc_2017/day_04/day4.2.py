#!/usr/bin/env python
import sys

def main(target_file):
    with open(target_file, 'r') as input_file:
        passphrases = input_file.read().split('\n')

    print('There are {} passphrases loaded for analysis'.format(len(passphrases)))
    passphrases_new = [[''.join(sorted(element)) for element in passphrase.split()] for passphrase in passphrases[:-1]]
    good_count = len([passphrase for passphrase in passphrases_new if
            len(passphrase) == len(list(set(passphrase)))])
    print('{} valid passphrases'.format(good_count))


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
