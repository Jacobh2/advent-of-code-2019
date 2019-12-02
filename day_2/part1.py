def _read_input(path):
    with open(path, "r") as f:
        return list(map(int, f.read().split(",")))


def halt(pc, opcodes):
    global running
    running = False


def add(pc, opcodes):
    # z = x + y
    x_pos, y_pos, z_pos = opcodes[pc + 1 : pc + 1 + 3]
    opcodes[z_pos] = opcodes[x_pos] + opcodes[y_pos]


def mul(pc, opcodes):
    # z = x + y
    x_pos, y_pos, z_pos = opcodes[pc + 1 : pc + 1 + 3]
    opcodes[z_pos] = opcodes[x_pos] * opcodes[y_pos]


functions = {99: halt, 1: add, 2: mul}

running = True


def execute_intcomputer(opcodes):
    global running, functions

    running = True
    pc = 0

    while running:
        opcode = opcodes[pc]
        fn = functions[opcode]

        fn(pc, opcodes)

        pc += 4

    print("Program halted")
    return opcodes


if __name__ == "__main__":
    opcodes = _read_input("input.txt")
    opcodes[1] = 12
    opcodes[2] = 2
    output = execute_intcomputer(opcodes)
    print("Pos0", output[0])

