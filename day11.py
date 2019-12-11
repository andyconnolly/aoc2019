class robot():
    def __init__(self, start, debug=None):
        self.x = 0
        self.y = 0
        self.dir = 0  #0 - up, 1 - right, 2 - down, 3 - left
        self.paintedBlack = []
        self.paintedWhite = []
        self.whitePanels = set()
        self.debug = True if debug == None else False
        if start == 1:
            self.paint(1)
    
    def getLocation(self):
        return "At (" + str(self.x) + ", " + str(self.y) + "), facing " + self.getDirection(self.dir)
    
    def getDirection(self, n):
        return ("up", "right", "down", "left")[n]
    
    def turn(self, n):
        if self.debug: print(self.getLocation(), "- Turn", "left" if n == 0 else "right") 
        if n == 0:
            self.dir = ((self.dir - 1) if (self.dir > 0) else 3)
            self.forward()
        elif n == 1:
            self.dir = ((self.dir + 1) if (self.dir < 3) else 0)
            self.forward()
        else:
            print("Invalid turn input:", n)
        if self.debug: print("    Result: ", self.getLocation())
    
    def paint(self, n):
        if self.debug: print(self.getLocation(), "- Paint", "black" if n == 0 else "white") 
        pos = (self.x, self.y)
        if n == 0:
            self.paintedBlack.append(pos)
            self.whitePanels.discard(pos)
        elif n == 1:
            self.paintedWhite.append(pos)
            self.whitePanels.add(pos)
        else:
            print("Invalid paint input:", n)
        if self.debug: print(str(len(self.whitePanels)), "White Panel(s)") #, self.whitePanels) 
    
    def forward(self):
        if self.dir == 0:
            self.y +=1
        elif self.dir == 1:
            self.x +=1
        elif self.dir == 2:
            self.y -= 1
        elif self.dir == 3:
            self.x -= 1
        else:
            print("Invalid direction")
    
    def getOutput(self):
        retVal = 1 if ((self.x, self.y) in self.whitePanels) else 0
        if self.debug: print("Asked for my output")
        if self.debug: print("    ", self.getLocation(), "- returning", retVal)
        return retVal

def value(data, state, idx):
    mode = str(data[state[0]])[:-2].zfill(3)[-idx]
    return data[state[0]+idx] if (mode == '0') else (state[0]+idx if (mode == '1') else data[state[0]+idx] + state[1])

def test(state, data, R):
    while data[state[0]] != 99:
        #input(str(data[state[0]:state[0]+4]) + "?")
        if data[state[0]] < 10:
            code = str(data[state[0]]).zfill(2)
        else:
            code = str(data[state[0]])[-2:]
        if code == '01':
            data[value(data, state, 3)] = data[value(data, state, 1)] + data[value(data, state, 2)]
            state[0] += 4
        elif code == '02':
            data[value(data, state, 3)] = data[value(data, state, 1)] * data[value(data, state, 2)]
            state[0] += 4
        elif code == '03':
            data[value(data, state, 1)] = R.getOutput()
            state[0] += 2
        elif code == '04':
            output = data[value(data, state, 1)]
            state[3].append(output)
            state[0] += 2
            return output
        elif code == '05':
            state[0] = (state[0] + 3) if (data[value(data, state, 1)] == 0) else data[value(data, state, 2)]
        elif code == '06':
            state[0] = (state[0] + 3) if (data[value(data, state, 1)] != 0) else data[value(data, state, 2)]
        elif code == '07':
            data[value(data, state, 3)] = 1 if (data[value(data, state, 1)] < data[value(data, state, 2)]) else 0
            state[0] += 4
        elif code == '08':
            data[value(data, state, 3)] = 1 if (data[value(data, state, 1)] == data[value(data, state, 2)]) else 0
            state[0] += 4
        elif code == '09':
            state[1] += data[value(data, state, 1)]
            state[0] += 2
        else:
            print("error - found code",code,"at position",state[0],"- data is:",data[state[0]])
            break
    return -1

data = [int(x) for x in open("day11input.txt", "r").readline().strip().split(',')]
data.extend([0]*1000)

for x in range(2):
    not_done = True
    d = data[:]
    R = robot(x, False)
    state = [0, 0, [], []]    #(position, relative position, input list, outputs)
    while not_done: 
        result = test(state, d, R)
        if result != -1: R.paint(result)
        result = test(state, d, R)
        if result != -1: R.turn(result)
        if result == -1 or d[state[0]] == 99:
            not_done = False
            if x == 0: 
                print("Part 1")
                print(len(set(R.paintedWhite).union(set(R.paintedBlack))))
            else:
                print("Part 2")
                xmin, xmax, ymin, ymax = 1000000, -1000000, 1000000, -1000000
                for p in R.whitePanels:
                    if p[0] < xmin: xmin = p[0]
                    if p[0] > xmax: xmax = p[0]
                    if p[1] < ymin: ymin = p[1]
                    if p[1] > ymax: ymax = p[1]
                grid = []
                for row in range(ymin, ymax + 1):
                    grid.append([])
                    for col in range(xmin, xmax + 1):
                        grid[-1].append(' ')
                for p in R.whitePanels:
                    grid[p[1]-ymin][p[0] - xmin] = '#'
                for g in grid[::-1]:
                    print("".join(g))

