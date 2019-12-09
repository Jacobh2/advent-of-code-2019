from collections import defaultdict

try:
    import part1
except ImportError:
    import day_6.part1 as part1


def calculate_orbit_jumps(input_str):
    inputs = input_str.split(",")
    planets = dict(map(lambda k: k.split(")"), inputs))
    reverse = dict(map(lambda k: k.split(")")[::-1], inputs))

    leaves = part1.find_leaves(planets, reverse)

    chain = defaultdict(list)
    for leaf in leaves:
        part1.go(leaf, reverse, chain)

    you = chain["YOU"]
    san = chain["SAN"]

    you_i = 0
    you_o = None
    for i, o in enumerate(you):
        if o in san:
            you_i = i
            you_o = o
            break

    return you_i + san.index(you_o)


if __name__ == "__main__":
    input_str = part1._read_file("day_6/input.txt")

    jumps = calculate_orbit_jumps(input_str)
    print("Jumps:", jumps)
