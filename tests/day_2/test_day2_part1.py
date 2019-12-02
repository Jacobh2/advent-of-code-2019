import day_2.part1


def test_execute_intcomputer():
    input_execute_intcomputer = [
        [1, 0, 0, 0, 99],
        [2, 3, 0, 3, 99],
        [2, 4, 4, 5, 99, 0],
        [1, 1, 1, 4, 99, 5, 6, 0, 99],
    ]
    output_execute_intcomputer = [
        [2, 0, 0, 0, 99],
        [2, 3, 0, 6, 99],
        [2, 4, 4, 5, 99, 9801],
        [30, 1, 1, 4, 2, 5, 6, 0, 99],
    ]

    for x, y in zip(input_execute_intcomputer, output_execute_intcomputer):
        print("________")
        assert day_2.part1.execute_intcomputer(x) == y

