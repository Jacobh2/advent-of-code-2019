class Direction:
    direction: str
    steps: int

    def __init__(self, part):
        self.direction = part[0]
        self.steps = int(part[1:])

    def __str__(self):
        return "{}{}".format(self.direction, self.steps)


def _read_input(path):
    with open(path, "r") as f:
        raw = f.read()
    return raw.split("\n")


def _convert_to_direction(wires):
    return list(map(Direction, wires.split(",")))


def _calculate_coordinate(position, wire):
    if wire.direction == "U":
        position[1] += wire.steps
    elif wire.direction == "D":
        position[1] -= wire.steps
    elif wire.direction == "L":
        position[0] -= wire.steps
    elif wire.direction == "R":
        position[0] += wire.steps


def _add_steps(positions, previous_position, position, for_x):
    if for_x:
        x = previous_position[0]
        step = -1 if previous_position[1] > position[1] else 1
        start_y = previous_position[1]
        end_y = position[1]
        for y in range(start_y, end_y, step):
            if isinstance(positions, list):
                if (x, y) not in positions:
                    positions.append((x, y))
            else:
                positions.add((x, y))
    else:
        y = previous_position[1]
        step = -1 if previous_position[0] > position[0] else 1
        start_x = previous_position[0]
        end_x = position[0]
        for x in range(start_x, end_x, step):
            if isinstance(positions, list):
                if (x, y) not in positions:
                    positions.append((x, y))
            else:
                positions.add((x, y))


def play_wire(origin, wires):
    positions = set()
    position = list(origin)
    previous_position = list(origin)
    for wire in wires:
        _calculate_coordinate(position, wire)
        _add_steps(positions, previous_position, position, wire.direction in {"D", "U"})
        previous_position = list(position)
        positions.add(tuple(position))

    return positions


def get_intersections(played_1, played_2):
    return played_1.intersection(played_2)


def manhattan_distance(origin, position):
    x_distance = 0
    y_distance = 0
    if position[0] > origin[0]:
        x_distance = position[0] - origin[0]
    else:
        x_distance = origin[0] - position[0]
    if position[1] > origin[1]:
        y_distance = position[1] - origin[1]
    else:
        y_distance = origin[1] - position[1]
    return x_distance + y_distance


def calculate_best_intersection(wires1, wires2):
    origin = (0, 0)
    p1 = play_wire(origin, _convert_to_direction(wires1))
    p2 = play_wire(origin, _convert_to_direction(wires2))
    ins = get_intersections(p1, p2)
    if origin in ins:
        ins.remove(origin)
    mds = [manhattan_distance(origin, i) for i in ins]
    return min(mds)


if __name__ == "__main__":
    w1, w2 = _read_input("day_3/input.txt")
    print("Best:", calculate_best_intersection(w1, w2))
