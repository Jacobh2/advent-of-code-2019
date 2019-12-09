def _read_input(path):
    with open(path, "r") as f:
        return list(map(int, f.read().split(",")))


def _get_value(param, value, opcodes):
    if param == 0:
        address = value % len(opcodes)
        # Address
        return opcodes[address]
    elif param == 1:
        # Immediate
        return value
    raise Exception("Unknown param {}".format(param))


def halt(args, params, opcodes):
    return False, None, None


def _store(address, value, opcodes):
    opcodes[address] = value


def add(args, params, opcodes):
    # z = x + y
    x_value = _get_value(params[0], args[0], opcodes)
    y_value = _get_value(params[1], args[1], opcodes)
    z_value = args[2]
    _store(z_value, x_value + y_value, opcodes)
    return True, None, None


def mul(args, params, opcodes):
    # z = x + y
    x_value = _get_value(params[0], args[0], opcodes)
    y_value = _get_value(params[1], args[1], opcodes)
    z_value = args[2]
    _store(z_value, x_value * y_value, opcodes)
    return True, None, None


def store(args, params, opcodes, get_input=lambda: int(input("Input: "))):
    address = args[0]
    value = get_input()
    _store(address, value, opcodes)
    return True, None, None


def pprint(args, params, opcodes, print_output=True):
    if params[0] == 0:
        value = opcodes[args[0]]
    else:
        value = args[0]
    if print_output:
        print("Computer Output:", value)
    return value == 0, None, value


functions = {99: (halt, 0), 1: (add, 3), 2: (mul, 3), 3: (store, 1), 4: (pprint, 1)}


def execute_intcomputer(
    opcodes, get_input_fn=None, print_output=True, continue_pc=None, name=None
):
    if continue_pc:
        pc = continue_pc
    else:
        pc = 0

    output = None
    while True:
        opcode_parts = opcodes[pc]
        opcode_parts_str = str(opcode_parts)
        opcode = int(opcode_parts_str[-2:])

        fn, num_params = functions[opcode]

        # Format params
        params = list(map(int, list(opcode_parts_str[:-2])))
        pad_num = num_params - len(params)
        params = ([0] * pad_num + params)[:num_params][::-1]

        # format args
        args = opcodes[pc + 1 : pc + 1 + num_params]

        if fn == pprint:
            should_continue, new_pc, output_ = fn(
                args, params, opcodes, print_output=print_output
            )
        elif fn == store and get_input_fn is not None:
            should_continue, new_pc, output_ = fn(
                args, params, opcodes, get_input=get_input_fn
            )
        else:
            should_continue, new_pc, output_ = fn(args, params, opcodes)

        if output_ is not None:
            output = output_

        if not should_continue:
            break

        if new_pc:
            pc = new_pc
        else:
            pc += 1 + num_params

    return opcodes, output, pc


if __name__ == "__main__":
    from sys import argv
    from os.path import join

    opcodes = _read_input("input.txt")

    execute_intcomputer(opcodes)
