def _read_input(path):
    with open(path, "r") as f:
        return list(map(int, f.read().split(",")))


def _get_value(param, value, opcodes):
    if param == 0:
        address = value % len(opcodes)
        print(
            "Parameterized mode, getting value at position",
            value,
            "address",
            address,
            "=",
            opcodes[address],
        )
        # Address
        return opcodes[address]
    elif param == 1:
        print("Immediate mode, getting value", value, "directly")
        # Immediate
        return value
    raise Exception("Unknown param {}".format(param))


def halt(args, params, opcodes):
    return False


def _store(address, value, opcodes):
    print("Storing", value, "at addr", address)
    opcodes[address] = value


def add(args, params, opcodes):
    # z = x + y
    x_value = _get_value(params[0], args[0], opcodes)
    y_value = _get_value(params[1], args[1], opcodes)
    z_value = args[2]  # _get_value(params[2], args[2], opcodes)
    _store(z_value, x_value + y_value, opcodes)
    return True


def mul(args, params, opcodes):
    # z = x + y
    x_value = _get_value(params[0], args[0], opcodes)
    y_value = _get_value(params[1], args[1], opcodes)
    z_value = args[2]  # _get_value(params[2], args[2], opcodes)
    _store(z_value, x_value * y_value, opcodes)
    return True


def store(args, params, opcodes):
    address = args[0]  # _get_value(params[0], args[0], opcodes)
    value = int(input("Input: "))
    _store(address, value, opcodes)
    return True


def pprint(args, params, opcodes):
    if params[0] == 0:
        value = opcodes[args[0]]
    else:
        value = args[0]
    # address = _get_value(params[0], args[0], opcodes)
    print("    >>>> Output:", value)
    return value == 0


functions = {99: (halt, 0), 1: (add, 3), 2: (mul, 3), 3: (store, 1), 4: (pprint, 1)}


def execute_intcomputer(opcodes):
    pc = 0
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

        if not fn(args, params, opcodes):
            print("Halting at pc", pc)
            break

        pc += 1 + num_params

    return opcodes


if __name__ == "__main__":
    from sys import argv
    from os.path import join

    # folder_path = argv[0].split("/")[0]
    # opcodes = _read_input(join(folder_path, "input.txt"))
    opcodes = _read_input("input.txt")

    execute_intcomputer(opcodes)
