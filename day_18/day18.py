#!/usr/bin/env python3
import sys
from collections import defaultdict

def parse_file(input_file):
    with open(input_file, 'r') as input_file:
        directions = []
        for line in input_file:
            directions.append(tuple([direction.strip() for direction in line.split()]))
    return directions

class Compiler(object):
    def __init__(self, instructions):
        self.env = defaultdict(int)
        self.instructions = instructions
        self.last_played = None
        self.index = 0


    def get_value(self, value):
        try:
            value = int(value)
        except ValueError:
            value = self.env[value]

        return value


    def next(self, bump=1):
        self.index += bump


    def current_step(self):
        if self.index < 0 or self.index > len(self.instructions) - 1:
            return None
        else:
            return self.instructions[self.index]


    def snd(self, value):
        self.last_played = self.env[value]
        self.next()


    def add(self, target, value):
        self.env[target] = self.get_value(target) + self.get_value(value)
        self.next()


    def mul(self, target, value):
        self.env[target] = self.get_value(target) * self.get_value(value)
        self.next()


    def mod(self, target, value):
        self.env[target] = self.get_value(target) % self.get_value(value)
        self.next()


    def jgz(self, target, value):
        if self.get_value(target) != 0:
            self.next(int(value))
        else:
            self.next()


    def set(self, target, value):
        self.env[target] = self.get_value(value)
        self.next()


    def rcv(self, target):
        if self.env[target] != 0:
            self.next()
            return self.last_played
        else:
            self.next()
            return None

def main(input_file):
    instructions = parse_file(input_file)
    compiler = Compiler(instructions)
    while compiler.current_step():
        if len(compiler.current_step()) == 3:
            method, target, value = compiler.current_step()
            getattr(compiler, method)(target, value)
        elif len(compiler.current_step()) == 2:
            method, target = compiler.current_step()
            if getattr(compiler, method)(target):
                break
    print(compiler.last_played)

if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
