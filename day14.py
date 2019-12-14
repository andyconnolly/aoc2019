from collections import defaultdict
from math import ceil

def parse(file):
    data = [x.strip().split(' => ') for x in open(file, "r").readlines()]
    retVal = dict()
    for i, o in data:
        outAmt, outName = o.split()
        inputs = []
        for x in i.split(', '):
            inAmt, inName = x.split()
            inputs.append((int(inAmt), inName))
        retVal[outName] = (int(outAmt), inputs)
    return retVal

def minOre(data, material, unitsRequired, leftovers):
    if material == 'ORE': return unitsRequired
    leftover = min(unitsRequired, leftovers[material])
    unitsRequired -= leftover
    leftovers[material] -= leftover
    created, inputs = data[material]
    n = ceil(unitsRequired / created)
    ore = 0
    for needed, input in inputs:
        ore += minOre(data, input, (n * needed), leftovers)
    leftovers[material] += (n * created) - unitsRequired
    return ore

def maxFuel(data, oreAvailable):
    l = None
    u = 1
    leftovers = defaultdict(int)
    while minOre(data, 'FUEL', u, leftovers) < oreAvailable:
        l = u
        u *= 2
    # Binary search to find maximum fuel produced, which must be between l and u.
    leftovers = defaultdict(int)
    while l < u:
        m = (l + u) // 2
        ore = minOre(data, 'FUEL', m, leftovers)
        if ore > oreAvailable:
            u = m
        elif ore < oreAvailable:
            l = m
    return l

data = parse('day14input.txt')
print('Part 1')
print(minOre(data, 'FUEL', 1, defaultdict(int)))
print('Part 2')
print(maxFuel(data, 1000000000000))
