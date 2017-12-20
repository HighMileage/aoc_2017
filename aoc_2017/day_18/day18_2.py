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
    def __init__(self, prog_id, partner_id, instructions, queue):
        self.env = defaultdict(int)
        self.partner_id = partner_id
        self.prog_id = prog_id
        self.instructions = instructions
        self.queue = queue
        self.index = 0

        self.env['p'] = prog_id


    def stalled(self):
        return not self.current_step() or (self.current_step()[0] == 'rcv' and self.messages() == [])


    def messages(self):
        return [msg for msg in self.queue if msg[0] == self.prog_id]


    def enque(self, value):
        self.queue.append((self.partner_id, value))
        self.next()


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
        # print('Sending {} the payload: {}'.format(value, payload))
        payload = self.get_value(value)
        self.enque(payload)


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
        if self.get_value(target) > 0:
            self.next(int(self.get_value(value)))
        else:
            self.next()


    def set(self, target, value):
        self.env[target] = self.get_value(value)
        self.next()


    def rcv(self, target):
        for recipient, payload in self.messages()[:1]:
            index = self.queue.index((recipient, payload))
            self.queue.pop(index)
            self.set(target, payload)

def run_compilers(compilers):
    compiler_0, compiler_1 = compilers
    send_count = 0
    queue = compiler_0.queue

    # Ensure that both compilers are not stalled and at least one has a next_step
    while not (compiler_0.stalled() and compiler_1.stalled()) and (compiler_0.current_step() or
            compiler_1.current_step()):
        # print('Initial queue state is {}'.format(queue))
        # print('C0 insturctions: {}'.format(compiler_0.current_step()))
        # print('C1 insturctions: {}'.format(compiler_1.current_step()))
        for compiler in compilers:
            command = compiler.current_step()
            if len(command) == 3:
                method, target, value = command
                getattr(compiler, method)(target, value)
            elif len(command) == 2:
                method, target = command
                if compiler.prog_id == 1 and command[0] == 'snd': send_count += 1
                getattr(compiler, method)(target)
    print('Final C0 insturctions: {}'.format(compiler_0.current_step()))
    print('Final queue: {}'.format(queue))
    print('Final C1 insturctions: {}'.format(compiler_1.current_step()))
    print(send_count)


def main(input_file):
    instructions = parse_file(input_file)
    my_queue = []
    compiler_0 = Compiler(0, 1, instructions, my_queue)
    compiler_1 = Compiler(1, 0, instructions, my_queue)
    compilers = [compiler_0, compiler_1]

    run_compilers(compilers)


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
