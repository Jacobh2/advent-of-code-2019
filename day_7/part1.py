from day_5 import part2
from itertools import permutations


def main(opcodes, num_phases=5):
    outputs = list()
    for phases in permutations(range(num_phases)):
        output = 0
        for phase in range(num_phases):
            input_iter = iter([phases[phase], output])

            def input_fn():
                v = next(input_iter)
                return v

            output = part2.part1.execute_intcomputer(opcodes, input_fn, False)[1]

        outputs.append((output, phases))

    outputs.sort(key=lambda i: i[0], reverse=True)
    return outputs[0]


def _load_opcodes(path):
    with open("day_7/input.txt", "r") as f:
        input_str = f.read()
    return list(map(int, input_str.split(",")))


if __name__ == "__main__":
    opcodes = _load_opcodes("day_7/input.txt")
    print(main(opcodes))
