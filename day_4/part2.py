from collections import Counter

try:
    import part1
except ImportError:
    import day_4.part1 as part1


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

    code_counter = Counter(code_list)
    most_common = code_counter.most_common(1)
    most_common_amount = most_common[0][1]

    # Never two of the same
    if most_common_amount == 1:
        return False

    # Any group of numbers that is 2
    group_lengths = [v for k, v in code_counter.items()]
    return 2 in group_lengths


if __name__ == "__main__":
    amount = 0
    low, high = part1._read_input("day_4/input.txt")
    for i in range(low, high + 1):
        if is_allowed(i, low, high):
            amount += 1

    print("Amount:", amount)
