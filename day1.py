data = [int(x) for x in open("day1input.txt", "r")] 
fuel = 0
for x in data:
    fuel += (x//3)-2

print(fuel)

def totalFuel(mass):
    total = 0
    fuel = (mass//3)-2
    while fuel > 0:
        total = total + fuel
        fuel = (fuel//3)-2
    return total

total = 0
for x in data:
    fuel = (x//3)-2
    total = total + fuel + totalFuel(fuel)

print(total)
