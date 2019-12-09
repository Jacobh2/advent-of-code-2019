import computer
from queue import Queue

def create_computer(opcodes):
    queue_in = Queue()
    queue_out = Queue()

    com = computer.IntComputer(opcodes, "A", queue_in, queue_out)
    com.start()
    return com, queue_in, queue_out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_str = f.read()

    opcodes = list(map(int, input_str.split(",")))

    pc, qin, qout = create_computer(opcodes)

    qin.put(2)
    pc.join()
    
    print(list(qout.queue))
