import day_1.part1


def test_calculate_fuel():
    input_calculate_total_fuel = [12, 14, 1969, 100756]
    output_calculate_total_fuel = [2, 2, 654, 33583]

    for x, y in zip(input_calculate_total_fuel, output_calculate_total_fuel):
        assert day_1.part1.calculate_fuel(x) == y


def caculate_total_fuel():
    input_calculate_total_fuel = [12, 14, 1969, 100756]
    output_calculate_total_fuel = 34241

    assert (
        day_1.part1.caculate_total_fuel(input_calculate_total_fuel)
        == output_calculate_total_fuel
    )
