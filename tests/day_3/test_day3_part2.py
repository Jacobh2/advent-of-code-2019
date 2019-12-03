import day_3.part2


def test_calculate_time_shortest_intersection():
    input_calculate_time_shortest_intersection = [
        ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"],
        [
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        ],
        ["R8,U5,L5,D3", "U7,R6,D4,L4"],
    ]
    output_calculate_time_shortest_intersection = [610, 410, 30]

    for x, y in zip(
        input_calculate_time_shortest_intersection,
        output_calculate_time_shortest_intersection,
    ):
        assert day_3.part2.calculate_time_shortest_intersection(x[0], x[1]) == y

