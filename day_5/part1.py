def _read_input(path):
    with open(path, "r") as f:
        return list(map(int, f.read().split(",")))


def _get_value(param, value, opcodes):
    if param == 0:
        address = value%len(opcodes)
        print("Parameterized mode, getting value at position", value, "address", address, "=", opcodes[address])
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
    z_value = args[2]#_get_value(params[2], args[2], opcodes)
    print("ADD x", x_value, "y", y_value, "z", z_value)
    _store(z_value, x_value + y_value, opcodes)
    return True


def mul(args, params, opcodes):
    # z = x + y
    x_value = _get_value(params[0], args[0], opcodes)
    y_value = _get_value(params[1], args[1], opcodes)
    z_value = args[2]#_get_value(params[2], args[2], opcodes)
    print("MUL x", x_value, "y", y_value, "z", z_value)
    _store(z_value, x_value * y_value, opcodes)
    return True


def store(args, params, opcodes):
    address = args[0]#_get_value(params[0], args[0], opcodes)
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
    if value != 0:
        # Check the instruction before this one!
        return -1
    return True #opcodes[address] == 0


functions = {99: (halt, 0), 1: (add, 3), 2: (mul, 3), 3: (store, 1), 4: (pprint, 1)}


def execute_intcomputer(opcodes):
    pc = 0
    while True:
        print("-"*10)
        print("PC:", pc)
        opcode_parts = opcodes[pc]
        print("OPPart:", opcode_parts)
        opcode_parts_str = str(opcode_parts)
        opcode = int(opcode_parts_str[-2:])

        fn, num_params = functions[opcode]

        # Format params
        params = list(map(int, list(opcode_parts_str[:-2])))
        print("!!!!! PARAMS:", params)
        pad_num = num_params - len(params)
        print("pad_num:", pad_num)
        params = ([0] * pad_num + params)[:num_params][::-1]

        # format args
        args = opcodes[pc + 1 : pc + 1 + num_params]

        print(
            "OPCODE", opcode, "have", num_params, "args:", args, "and params:", params
        )

        ans = fn(args, params, opcodes)
        if ans == -1:
            print("Previous opcode:")
            break
        elif not ans:
            print("Halting at pc", pc)
            break
        
        # if pc == 20:
        #     break
        pc += 1 + num_params
        print("-"*10)

    return opcodes


if __name__ == "__main__":
    from sys import argv
    from os.path import join

    # folder_path = argv[0].split("/")[0]
    # opcodes = _read_input(join(folder_path, "input.txt"))
    opcodes = _read_input("input.txt")
    print("opcodes:", opcodes[:50])

    output = execute_intcomputer(opcodes)
    print("Pos0", output[0])

    """
    [
        #0
        3, 225, # Store 1 at address where 225 is pointing at
        #2
        1, 225, 6, 6, # Add what is stored at 225 with what is stored at 6, and place at 6
        #6
        1100, 1, 238, 225, 104, 0, 1102, 72, 20, 224, 1001, 224, -1440, 224, 4, 224, 102, 8, 223

    """

