from collections import defaultdict


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
    for batch in group_list(image, width * height):
        count = batch.count("0")
        if count < min_number:
            min_number = count
            saved_batch = batch

    return saved_batch.count("1") * saved_batch.count("2")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        image = f.read()

    print("Result:", main(image))
