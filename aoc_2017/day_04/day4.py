#!/usr/bin/env python
import sys

def main(target_file):
    with open(target_file, 'r') as input_file:
        passphrases = input_file.read().split('\n')
        print('There are {} passphrases loaded for analysis'.format(len(passphrases)))
        good_count = len([passphrase for passphrase in passphrases[:-1] if
                len(passphrase.split()) == len(list(set(passphrase.split())))])
    print('{} valid passphrases'.format(good_count))


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
