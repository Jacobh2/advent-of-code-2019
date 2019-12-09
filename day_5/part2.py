try:
    import part1
except ImportError:
    from day_5 import part1


def jump_if_true(args, params, opcodes):
    check_value = part1._get_value(params[0], args[0], opcodes)
    jumpt_to = part1._get_value(params[1], args[1], opcodes)
    return True, jumpt_to if check_value != 0 else None, None


def jump_if_false(args, params, opcodes):
    check_value = part1._get_value(params[0], args[0], opcodes)
    jumpt_to = part1._get_value(params[1], args[1], opcodes)
    return True, jumpt_to if check_value == 0 else None, None


def less_than(args, params, opcodes):
    first = part1._get_value(params[0], args[0], opcodes)
    second = part1._get_value(params[1], args[1], opcodes)
    address = args[2]  # part1._get_value(params[2], args[2], opcodes)
    if first < second:
        part1._store(address, 1, opcodes)
    else:
        part1._store(address, 0, opcodes)
    return True, None, None


def equals(args, params, opcodes):
    first = part1._get_value(params[0], args[0], opcodes)
    second = part1._get_value(params[1], args[1], opcodes)
    address = args[2]  # part1._get_value(params[2], args[2], opcodes)
    if first == second:
        part1._store(address, 1, opcodes)
    else:
        part1._store(address, 0, opcodes)
    return True, None, None


part1.functions[5] = (jump_if_true, 2)
part1.functions[6] = (jump_if_false, 2)
part1.functions[7] = (less_than, 3)
part1.functions[8] = (equals, 3)


if __name__ == "__main__":
    from sys import argv
    from os.path import join

    opcodes = part1._read_input("input.txt")
    part1.execute_intcomputer(opcodes)
