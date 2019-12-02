import { readFile } from 'fs';
import { join } from 'path';

var filePath = join(process.cwd(), process.argv[2], 'input.txt');

function calculateFuel(mass) {
    var fuel = Math.floor(mass / 3) - 2;
    if (fuel <= 0) {
        return 0;
    }
    return fuel + calculateFuel(fuel);
}

readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (!err) {
        var fuelRequired = data
            .split("\n")
            .map((fuel) => parseInt(fuel))
            .map(calculateFuel)
            .reduce((total, fuel) => total + fuel);
        console.log("Required fuel:", fuelRequired);
    } else {
        console.log("Error reading file:", err);
    }
});
