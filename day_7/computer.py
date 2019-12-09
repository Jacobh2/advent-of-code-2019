from threading import Thread
from queue import Queue


class IntComputer(Thread):
    def __init__(self, opcodes, name, input_queue, output_queue):
        super().__init__(name=name, daemon=True)
        self.input = input_queue
        self.output = output_queue
        self.running = True
        self.pc = 0
        self.skip_update_pc = False
        self.opcodes = opcodes.copy()
        self.functions = {
            99: (self.halt, 0),
            1: (self.add, 3),
            2: (self.mul, 3),
            3: (self.store, 1),
            4: (self.pprint, 1),
            5: (self.jump_if_true, 2),
            6: (self.jump_if_false, 2),
            7: (self.less_than, 3),
            8: (self.equals, 3),
        }
        self.last_output = None

    def _get_value(self, param, value):
        if param == 0:
            address = value % len(self.opcodes)
            # Address
            return self.opcodes[address]
        elif param == 1:
            # Immediate
            return value

    def halt(self, args, params):
        self.running = False

    def _store(self, address, value):
        self.opcodes[address] = value

    def add(self, args, params):
        x_value = self._get_value(params[0], args[0])
        y_value = self._get_value(params[1], args[1])
        z_value = args[2]
        self._store(z_value, x_value + y_value)
        self.pc += 1 + len(params)

    def mul(self, args, params):
        x_value = self._get_value(params[0], args[0])
        y_value = self._get_value(params[1], args[1])
        z_value = args[2]
        self._store(z_value, x_value * y_value)
        self.pc += 1 + len(params)

    def store(self, args, params):
        address = args[0]
        value = self.input.get()
        self._store(address, value)
        self.pc += 1 + len(params)

    def pprint(self, args, params):
        if params[0] == 0:
            value = self.opcodes[args[0]]
        else:
            value = args[0]
        self.last_output = value
        self.output.put_nowait(value)
        self.pc += 1 + len(params)

    def jump_if_true(self, args, params):
        check_value = self._get_value(params[0], args[0])
        jumpt_to = self._get_value(params[1], args[1])
        if check_value != 0:
            self.pc = jumpt_to
        else:
            self.pc += 1 + len(params)

    def jump_if_false(self, args, params):
        check_value = self._get_value(params[0], args[0])
        jumpt_to = self._get_value(params[1], args[1])
        if check_value == 0:
            self.pc = jumpt_to
        else:
            self.pc += 1 + len(params)

    def less_than(self, args, params):
        first = self._get_value(params[0], args[0])
        second = self._get_value(params[1], args[1])
        address = args[2]
        if first < second:
            self._store(address, 1)
        else:
            self._store(address, 0)
        self.pc += 1 + len(params)

    def equals(self, args, params):
        first = self._get_value(params[0], args[0])
        second = self._get_value(params[1], args[1])
        address = args[2]
        if first == second:
            self._store(address, 1)
        else:
            self._store(address, 0)
        self.pc += 1 + len(params)

    def _parse_opcode(self):
        opcode_parts = self.opcodes[self.pc]
        opcode_parts_str = str(opcode_parts)
        opcode = int(opcode_parts_str[-2:])
        fn, num_params = self.functions[opcode]

        # Format params
        params = list(map(int, list(opcode_parts_str[:-2])))
        pad_num = num_params - len(params)
        params = ([0] * pad_num + params)[:num_params][::-1]

        # format args
        args = self.opcodes[self.pc + 1 : self.pc + 1 + num_params]

        return fn, args, params

    def run(self):
        while self.running:
            fn, args, params = self._parse_opcode()
            fn(args, params)