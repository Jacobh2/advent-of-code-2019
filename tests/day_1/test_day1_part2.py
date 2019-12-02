import day_1.part2


def test_calculate_fuel():
    input_calculate_total_fuel = [14, 1969, 100756]
    output_calculate_total_fuel = [2, 966, 50346]

    for x, y in zip(input_calculate_total_fuel, output_calculate_total_fuel):
        assert day_1.part2.calculate_fuel(x) == y


def caculate_total_fuel():
    input_calculate_total_fuel = [12, 14, 1969, 100756]
    output_calculate_total_fuel = 51314

    assert (
        day_1.part2.caculate_total_fuel(input_calculate_total_fuel)
        == output_calculate_total_fuel
    )
