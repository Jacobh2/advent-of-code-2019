try:
    import computer
except ImportError:
    import day_7.computer as computer

from itertools import permutations
from queue import Queue


def main(opcodes):

    def create_computers():
        queues = [Queue(), Queue(), Queue(), Queue(), Queue()]

        a = computer.IntComputer(list(opcodes), "A", queues[0], queues[1])
        b = computer.IntComputer(list(opcodes), "B", queues[1], queues[2])
        c = computer.IntComputer(list(opcodes), "C", queues[2], queues[3])
        d = computer.IntComputer(list(opcodes), "D", queues[3], queues[4])
        e = computer.IntComputer(list(opcodes), "E", queues[4], queues[0])
        ts = [a, b, c, d, e]

        for t in ts:
            t.start()

        return ts, queues

    num_phases = 5
    phases_start = 5
    outputs = list()
    phases_ = permutations(list(range(phases_start, phases_start + num_phases)))

    outputs = list()
    for phases in phases_:
        ts, queues = create_computers()
        for phase, q in zip(phases, queues):
            q.put(phase)

        queues[0].put(0)

        for t in ts:
            t.join()

        outputs.append((ts[-1].last_output, phases))

    outputs.sort(key=lambda i: i[0], reverse=True)
    return outputs[0]


if __name__ == "__main__":

    with open("day_7/input.txt", "r") as f:
        input_str = f.read()

    opcodes = list(map(int, input_str.split(",")))
    result = main(opcodes)
    print("Result:", result[0], "with phases", result[1])

