from copy import deepcopy
from itertools import dropwhile


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


colors = {"1": " ", "2": "░", "0": "▉"}


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def main(image):
    width = 25
    height = 6

    layers = list(group_list(image, width * height))

    transparent = "2"

    layers_transposed = transpose(layers)

    final_image_flat = list()
    for l in layers_transposed:
        color_num = next(dropwhile(lambda i: i == transparent, l))
        final_image_flat.append(colors[color_num])

    for l in group_list(final_image_flat, width):
        print("".join(l))


if __name__ == "__main__":
    image = _read("input.txt")
    main(image)
