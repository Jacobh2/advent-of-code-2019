import computer
from queue import Queue

def create_computer(opcodes):
    queue_in = Queue()
    queue_out = Queue()

    com = computer.IntComputer(opcodes, "A", queue_in, queue_out)
    com.start()
    return com, queue_in, queue_out


if __name__ == "__main__":
    # opcodes = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    # opcodes = [1102,34915192,34915192,7,4,7,99,0]
    # opcodes = [104,1125899906842624,99]

    with open("input.txt", "r") as f:
        input_str = f.read()

    opcodes = list(map(int, input_str.split(",")))

    pc, qin, qout = create_computer(opcodes)

    qin.put(1)
    pc.join()
    
    #21108
    # op 8
    # param 0112
    print(list(qout.queue))
