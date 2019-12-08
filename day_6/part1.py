from collections import defaultdict
from collections import Counter


def _read_file(path):
    with open(path, "r") as f:
        return ",".join(f.read().split("\n"))


def find_leaves(right, left):
    leaves = set()
    for k in left.keys():
        if k not in right:
            leaves.add(k)
    return leaves


def go(leaf, reverse, chain):
    start = str(leaf)
    while leaf in reverse:
        leaf = reverse[leaf]
        chain[start].append(leaf)


check = {
    "C": 2,
    "L": 7,
    "F": 5,
    "D": 3,
    "J": 5,
    "E": 4,
    "H": 3,
    "B": 1,
    "I": 4,
    "G": 2,
    "K": 6,
}


def arithm_sum(length):
    return ((1 + length) / 2) * length


def find_similar(lists):
    c = Counter()
    root = lists[0][0]
    for part in lists:
        # A part can be [COM, B, G, H]
        # And we want to find [COM, B] since that exists in the others
        for i in range(len(part)):
            part_str = "-".join(part[:i])
            if not part_str or part_str == root:
                continue
            c[part_str] += 1

    ret = dict()
    for k, v in c.items():
        if v > 1:
            ret[k] = v - 1
    return ret


def calculate_checksum(input_str):
    inputs = input_str.split(",")
    planets = dict(map(lambda k: k.split(")"), inputs))
    reverse = dict(map(lambda k: k.split(")")[::-1], inputs))

    leaves = find_leaves(planets, reverse)

    chain = defaultdict(list)
    for leaf in leaves:
        go(leaf, reverse, chain)

    # 1 & 2
    all_costs = 0
    lists = list()
    for k, v in chain.items():
        total = v[::-1] + [k]
        all_costs += arithm_sum(len(v))
        lists.append(total)

    all_costs = int(all_costs)

    # 3
    to_be_removed = find_similar(lists)
    cost_to_remove = 0
    for key, cost in to_be_removed.items():
        cost_to_remove += (len(key.split("-"))-1) * cost

    return all_costs - cost_to_remove

if __name__ == "__main__":
    input_str = _read_file("input.txt")

    # input_str = "COM)BBB,BBB)CCC,CCC)DDD,DDD)EEE,EEE)FFF,BBB)GGG,GGG)HHH"

    total_cost = calculate_checksum(input_str) 

        #251208
    print("Total cost:", total_cost)
    exit(0)

