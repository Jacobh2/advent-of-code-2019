def calculate_fuel(mass):
    return mass // 3 - 2


def _read_masses(path):
    with open(path, "r") as f:
        return list(map(int, f.read().split("\n")))


def caculate_total_fuel(masses):
    return sum(map(calculate_fuel, masses))


if __name__ == "__main__":
    from sys import argv
    from os.path import join

    folder_path = argv[0].split("/")[0]
    masses = _read_masses(join(folder_path, "input.txt"))
    fuel_requires = caculate_total_fuel(masses)
    print(len(masses), "masses require", fuel_requires, "fuel")
