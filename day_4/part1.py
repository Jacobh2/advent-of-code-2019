from collections import Counter


def _read_input(path):
    with open("input.txt", "r") as f:
        return list(map(int, f.read().split("-")))


def is_allowed(code, low, high):
    code_str = str(code)

    # 6 digits
    if len(code_str) != 6:
        return False

    if low > code and code > high:
        return False

    code_list = list(code_str)
    sorted_list = "".join(sorted(code_list))
    # Never decreasing
    if sorted_list != code_str:
        return False

    # Never two of the same
    counter = Counter(code_list)
    if counter.most_common(1)[0][1] == 1:
        return False

    return True


if __name__ == "__main__":
    amount = 0
    low, high = _read_input("input.txt")
    for i in range(low, high + 1):
        if is_allowed(i, low, high):
            amount += 1

    print("Amount:", amount)
