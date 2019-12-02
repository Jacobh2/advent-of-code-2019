import part1


def find_noun_and_verb(opcodes, noun, verb):
    noun_index = 1
    verb_index = 2
    opcodes = opcodes.copy()

    opcodes[noun_index] = noun
    opcodes[verb_index] = verb

    output = part1.execute_intcomputer(opcodes)[0]
    return output


if __name__ == "__main__":
    from sys import argv
    from os.path import join

    folder_path = argv[0].split("/")[0]
    opcodes = part1._read_input(join(folder_path, "input.txt"))
    target = 19690720

    for noun in range(100):
        for verb in range(100):
            if target == find_noun_and_verb(opcodes, noun, verb):
                print("Found noun={} and verb={}".format(noun, verb))
                print("Result:", 100 * noun + verb)
