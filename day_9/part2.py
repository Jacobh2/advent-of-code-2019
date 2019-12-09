try:
    import part1
except ImportError:
    import day_9.part1 as part1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_str = f.read()

    opcodes = list(map(int, input_str.split(",")))

    print(part1.run_computer(opcodes, 2))
