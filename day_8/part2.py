from itertools import dropwhile

try:
    import part1
except ImportError:
    import day_8.part1 as part1


colors = {"1": " ", "2": "░", "0": "▉"}


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def main(image):
    width = 25
    height = 6

    layers = list(part1.group_list(image, width * height))

    transparent = "2"

    layers_transposed = transpose(layers)

    final_image_flat = list()
    for layer in layers_transposed:
        color_num = next(dropwhile(lambda i: i == transparent, layer))
        final_image_flat.append(colors[color_num])

    for line in part1.group_list(final_image_flat, width):
        print("".join(line))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        image = f.read()

    main(image)
