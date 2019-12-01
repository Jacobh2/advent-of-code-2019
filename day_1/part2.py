def caculate_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + caculate_fuel(fuel)

if __name__ == "__maain__":
    

