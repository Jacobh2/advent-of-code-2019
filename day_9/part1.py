try:
    import computer
except ImportError:
    import day_9.computer as computer
from queue import Queue


def create_computer(opcodes):
    queue_in = Queue()
    queue_out = Queue()

    com = computer.IntComputer(opcodes, "A", queue_in, queue_out)
    com.start()
    return com, queue_in, queue_out


def run_computer(opcodes, run_code):
    pc, qin, qout = create_computer(opcodes)
    qin.put(run_code)
    pc.join()
    return list(qout.queue)


if __name__ == "__main__":
    with open("day_9/input.txt", "r") as f:
        input_str = f.read()

    opcodes = list(map(int, input_str.split(",")))

    print("Result:", run_computer(opcodes, 1)[0])
