import day_6.part1 as part1


def test_part1():
    inputs = [
        "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L",
        "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,B)J,J)K,J)L,L)M",
        "COM)B,B)C,C)D,D)E,E)F,B)G,G)H",
    ]
    outputs = [42, 32, 20]

    for x, y in zip(inputs, outputs):
        assert part1.calculate_checksum(x) == y
