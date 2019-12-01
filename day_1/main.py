def calculate_fuel(mass):
    return mass // 3 - 2


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        masses = list(map(int, f.read().split("\n")))
    print(len(masses), "masses")
    fuel_requires = sum(map(calculate_fuel, masses))
    print("Fuel required:", fuel_requires)
