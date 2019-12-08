import day_6.part2 as part2


def test_part2():
    inputs = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L,K)YOU,I)SAN"
    outputs = 4

    assert part2.calculate_orbit_jumps(inputs) == outputs
