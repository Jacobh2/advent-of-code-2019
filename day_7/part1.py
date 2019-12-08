from day_5 import part2
from itertools import permutations


if __name__ == "__main__":

    # input_str = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    input_str = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    input_str = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"

    with open("day_7/input.txt", "r") as f:
        input_str = f.read()

    opcodes = list(map(int, input_str.split(",")))

    num_phases = 5
    outputs = list()
    #opcodes, get_input_fn=None, print_output=True
    for phases in permutations(range(num_phases)):
        output = 0
        for phase in range(num_phases):
            input_iter = iter([phases[phase], output])
            def input_fn():
                v = next(input_iter)
                return v
            opcodes, output = part2.part1.execute_intcomputer(opcodes, input_fn, False)
        outputs.append((output, phases))

    print("outputs:", outputs.sort(key=lambda i: i[0], reverse=True))
    print("Max:", outputs[0])
