try:
    import part1
except ImportError:
    import day_3.part1 as part1


def _add_steps(positions, previous_position, position, position_set, for_x):
    if for_x:
        x = previous_position[0]
        step = -1 if previous_position[1] > position[1] else 1
        start_y = previous_position[1]
        end_y = position[1]
        for y in range(start_y, end_y, step):
            if (x, y) not in position_set:
                positions.append((x, y))
            position_set.add((x, y))
    else:
        y = previous_position[1]
        step = -1 if previous_position[0] > position[0] else 1
        start_x = previous_position[0]
        end_x = position[0]
        for x in range(start_x, end_x, step):
            if (x, y) not in position_set:
                positions.append((x, y))
            position_set.add((x, y))


def play_wire(origin, wires):
    positions = list()
    positions_set = set()
    position = list(origin)
    previous_position = list(origin)
    for wire in wires:
        part1._calculate_coordinate(position, wire)
        _add_steps(
            positions,
            previous_position,
            position,
            positions_set,
            wire.direction in {"D", "U"},
        )
        previous_position = list(position)

        pp = tuple(position)
        if pp not in positions_set:
            positions.append(pp)
        positions_set.add(pp)

    return positions


def get_intersections(played_1, played_2):
    intersections = dict()
    pairs = list()
    for i, p in enumerate(played_1):
        intersections[p] = i
    for i, p in enumerate(played_2):
        if p in intersections:
            pairs.append((intersections[p], i))
    return pairs


def calculate_timing(steps):
    x_, y_ = steps[0]
    total = 0
    for x, y in steps:
        total += abs(x - x_)
        total += abs(y - y_)
        x_ = x
        y_ = y
    return total


def calculate_time_shortest_intersection(wires1, wires2):
    origin = (0, 0)
    p1 = play_wire(origin, part1._convert_to_direction(wires1))
    p2 = play_wire(origin, part1._convert_to_direction(wires2))
    ins = get_intersections(p1, p2)
    if origin in ins:
        ins.remove(origin)
    timings = [calculate_timing(p1[:i1]) + calculate_timing(p2[:i2]) for i1, i2 in ins]
    return min(timings) + 2


if __name__ == "__main__":
    w1, w2 = part1._read_input("day_3/input.txt")
    print("Best:", calculate_time_shortest_intersection(w1, w2))
