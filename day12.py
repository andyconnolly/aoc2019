from math import gcd

class Moon:
    def __init__(self, pos):
        x, y, z = [int(x.split('=')[1]) for x in pos[1:-1].split(', ')]
        self.pos = {'X': x, 'Y': y, 'Z': z}
        self.v = {'X': 0, 'Y': 0, 'Z': 0}
    
    def updateV(self, moon):
        for axis in self.pos:
            if self.pos[axis] < moon.pos[axis]:
                self.v[axis] += 1 
            elif self.pos[axis] > moon.pos[axis]:
                self.v[axis] -= 1
    
    def updatePos(self):
        for axis in self.pos:
            self.pos[axis] += self.v[axis]
    
    def potentialE(self): return sum([abs(pe) for pe in self.pos.values()])
    def kineticE(self):   return sum([abs(ke) for ke in self.v.values()])
    def totalE(self):     return self.potentialE() * self.kineticE()

class Moons:
    def __init__(self, file):
        self.moons = []
        lines = open(file, 'r').readlines()
        for line in lines:
            self.moons.append(Moon(line.strip()))
    
    def update(self):
        for moon1, moon2 in [(m1, m2) for m1 in self.moons for m2 in self.moons if m1 != m2]:
            moon1.updateV(moon2)
        for moon in self.moons:
            moon.updatePos()
    
    def totalE(self):
        return sum([moon.totalE() for moon in self.moons])
    
    def getState(self, axis):
        state = []
        for moon in self.moons:
            state.append(moon.pos[axis])
            state.append(moon.v[axis])
        return tuple(state)
    
    def repeatsOnAxis(self, axis):
        steps = 0
        previous = {self.getState(axis)}
        not_found = True
        while not_found:
            self.update()
            state = self.getState(axis)
            steps += 1
            if state in previous:
                return steps
        return steps

def stepsUntilRepeated(file):
    reps = {'X':0, 'Y':0, 'Z':0}
    for axis in reps.keys():
        moons = Moons(file)
        reps[axis] = moons.repeatsOnAxis(axis)
        print(axis + '-axis repeats:', str(reps[axis]))
    moons = Moons(file)
    LCMxy = (reps['X'] * reps['Y']) // gcd(reps['X'], reps['Y'])
    LCM = (LCMxy * reps['Z']) // gcd(LCMxy, reps['Z'])
    return LCM

print('Part 1')
state = Moons('day12input.txt')
for i in range(1000): state.update()

print(state.totalE())
print('Part 2')
steps = stepsUntilRepeated('day12input.txt')
print(steps)
