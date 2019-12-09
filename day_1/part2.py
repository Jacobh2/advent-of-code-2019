def calculate_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel(fuel)


def _read_masses(path):
    with open(path, "r") as f:
        return list(map(int, f.read().split("\n")))


def caculate_total_fuel(masses):
    return sum(map(calculate_fuel, masses))


if __name__ == "__main__":
    masses = _read_masses("day_1/input.txt")
    fuel_requires = caculate_total_fuel(masses)
    print(len(masses), "masses require", fuel_requires, "fuel")
