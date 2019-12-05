import day_5.part1


def test_execute_intcomputer():
    input_execute_intcomputer = [
        [1002, 4, 3, 4, 33],
        [1101, 100, -1, 4, 0]
        ]
    output_execute_intcomputer = [[1002, 4, 3, 4, 99], [1101, 100, -1, 4, 99]]

    for x, y in zip(input_execute_intcomputer, output_execute_intcomputer):
        assert day_5.part1.execute_intcomputer(x) == y
