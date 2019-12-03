import day_3.part1


def test_manhattan_distance():
    input_manhattan_distance = [
        [
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83",
        ],
        [
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        ],
        [
            "R8,U5,L5,D3",
            "U7,R6,D4,L4"
        ]
    ]
    output_manhattan_distance = [
        159,
        135,
        6
    ]

    for x, y in zip(input_manhattan_distance, output_manhattan_distance):
        assert day_3.part1.calculate_best_intersection(x[0], x[1]) == y

