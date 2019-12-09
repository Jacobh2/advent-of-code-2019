from collections import defaultdict
import operator


def _read(path):
    with open(path, "r") as f:
        return f.read()


def group_list(items, group_size):
    group = None
    for i, item in enumerate(items):
        if i % group_size == 0:
            if group is not None:
                yield group
            group = list()
        group.append(item)
    yield group


def main(image):
    width = 25
    height = 6

    min_number = 9999
    saved_batch = None
    for layer_index, batch in enumerate(group_list(image, width * height)):

        count = batch.count("0")
        if count < min_number:
            min_number = count
            saved_batch = batch

    ones = saved_batch.count("1")
    twos = saved_batch.count("2")
    print("Result:", ones * twos)


if __name__ == "__main__":
    image = _read("input.txt")
    main(image)
