try:
    import part1
except ImportError:
    import day_9.part1 as part1


if __name__ == "__main__":
    with open("day_9/input.txt", "r") as f:
        input_str = f.read()

    opcodes = list(map(int, input_str.split(",")))

    print("Result:", part1.run_computer(opcodes, 2)[0])
