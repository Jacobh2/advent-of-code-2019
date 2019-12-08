from day_5 import part2
from itertools import permutations
from threading import Thread
from queue import Queue


class AmplifierControllerSoftware(Thread):
    def __init__(self, phase, name, opcodes, next_queue):
        super().__init__(name=name, daemon=True)
        self.phase = phase
        self.msg = Queue(1)
        self.opcodes = opcodes
        self.next_queue = next_queue

    def run(self):
        try:
            running = True
            while running:
                print("Phase", self.name, "is waiting for new input")
                computer_input = self.msg.get()
                print("Phase", self.name, "got", computer_input)
                inputs = iter([self.phase, computer_input])
                def input_fn():
                    return next(inputs)
                _, output = part2.part1.execute_intcomputer(self.opcodes, input_fn, False)
                self.next_queue.put(output)
        except Exception as e:
            print("Crash in", self.name, e)


def main():
    # with open("day_7/input.txt", "r") as f:
    #     input_str = f.read()

    something_long = 139629729

    input_str = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"

    opcodes = list(map(int, input_str.split(",")))

    num_phases = 5
    phases_alpha = ["A", "B", "C", "D", "E"]
    phases_start = 5
    outputs = list()
    # opcodes, get_input_fn=None, print_output=True
    phases_ = permutations(list(range(phases_start, phases_start + num_phases)))

    phases_ = [[9, 7, 8, 5, 6]]

    acss = {
        0: [lambda input_fn: part2.part1.execute_intcomputer(list(opcodes), input_fn, True), 0],
        1: [lambda input_fn: part2.part1.execute_intcomputer(list(opcodes), input_fn, True), None],
        2: [lambda input_fn: part2.part1.execute_intcomputer(list(opcodes), input_fn, True), None],
        3: [lambda input_fn: part2.part1.execute_intcomputer(list(opcodes), input_fn, True), None],
        4: [lambda input_fn: part2.part1.execute_intcomputer(list(opcodes), input_fn, True), None]
    }

    for phases in phases_:
        output = 0
        while True:
            for phase_index, phase_name in enumerate(phases_alpha):
                print("Calculating for phase", phase_name)

                phase = phases[phase_index]
                computer, input_value = acss[phase_index]
                print("Phase", phase_name, "input:", input_value)

                inputs = [phase, input_value]
                input_iter = iter(inputs)

                def input_fn():
                    return next(input_iter)

                print("*** START ***")
                opcodes_, output = computer(input_fn)

                acss[(phase_index+1)%5][1] = output
                print("*** DONE ***", output)

        outputs.append((output, phases))

    outputs.sort(key=lambda i: i[0], reverse=True)
    print("Max:", outputs[0])


def threaded():
    input_str = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"

    opcodes = list(map(int, input_str.split(",")))

    phases_alpha = ["A", "B", "C", "D", "E"]
    phases = [9, 7, 8, 5, 6]
    ts = list()

    e = AmplifierControllerSoftware(phases[4], phases_alpha[4], opcodes, None)
    d = AmplifierControllerSoftware(phases[3], phases_alpha[3], opcodes, e.msg)
    c = AmplifierControllerSoftware(phases[2], phases_alpha[2], opcodes, d.msg)
    b = AmplifierControllerSoftware(phases[1], phases_alpha[1], opcodes, c.msg)
    a = AmplifierControllerSoftware(phases[0], phases_alpha[0], opcodes, b.msg)
    e.next_queue = a.msg

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    print("Starting!")
    a.msg.put(0)
    a.join()


if __name__ == "__main__":
    main()


    