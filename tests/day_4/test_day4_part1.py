import day_4.part1


def test_is_allowed():
    input_is_allowed = [111111, 223450, 123789]
    output_is_allowed = [True, False, False]

    for x, y in zip(input_is_allowed, output_is_allowed):
        assert day_4.part1.is_allowed(x, 0, 999999) == y

