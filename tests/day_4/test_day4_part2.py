import day_4.part2


def test_is_allowed():
    input_is_allowed = [112233, 123444, 111122]
    output_is_allowed = [True, False, True]

    for x, y in zip(input_is_allowed, output_is_allowed):
        assert day_4.part2.is_allowed(x, 0, 999999) == y

