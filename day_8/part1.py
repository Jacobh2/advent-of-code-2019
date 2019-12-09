from collections import defaultdict
import operator

def _read(path):
    with open(path, "r") as f:
        return f.read()


def main(image):
    layers = list()

    width = 25
    height = 6
    j = 0
    min_layer = 0
    max_numnber = 0
    for index, i in enumerate(range(0, len(image), width)):
        batch = image[i : i + width]

        layers.append((j, i, batch.count("0")))

        count = batch.count("0")
        if count >= max_numnber:
            min_layer = j
            max_numnber = count
            print("Batch:", batch)

        if index > 0 and index%height == 0:
            print("New layer")
            j += 1

        print("Layer", (j+1), "Batch:", batch)


    print(layers)
    layers.sort(key=operator.itemgetter(2), reverse=True)
    layers.sort(key=operator.itemgetter(0), reverse=False)
    print("layers:", layers)
    l = layers[0][0]
    print("Best layer:", l+1)
    l = 98*6
    print("Numbers:", image[l: l+width])
    print("Numbers:", image[l+1: l+1+width])

    print("min_layer:", min_layer)
    print("count:", max_numnber)


if __name__ == "__main__":
    image = _read("input.txt")
    print("Len:", len(image))
    # exit(0)
    # image = "123456789012"

    # Layer 299 is too low
    main(image)
