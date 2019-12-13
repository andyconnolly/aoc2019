def value(data, state, idx):
    mode = str(data[state[0]])[:-2].zfill(3)[-idx]
    return data[state[0]+idx] if (mode == '0') else (state[0]+idx if (mode == '1') else data[state[0]+idx] + state[1])

def test(state, data, mode=None):
    if mode == None: mode = 'MANUAL'
    while data[state[0]] != 99:
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
            if mode == 'MANUAL':
                display(state)
                inp = input("left:L, [stay:0], right:R ?")
                val = -1 if inp in {"L", "l"} else (1 if inp in {"R", 'r'} else 0)
                data[value(data, state, 1)] = val
            else:
                getInput(state)
                data[value(data, state, 1)] = state[2].pop()
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

def display(state):
    maxX = max(state[3][0::3]) + 2
    maxY = max(state[3][1::3]) + 2
    score = 0
    grid = []
    for y in range(maxY):
        grid.append([])
        for x in range(maxX):
            grid[-1].append(' ')
    try:
        for pos in range(0, len(state[3]), 3):
            if pos + 2 <= len(state[3]):
                x, y, ob = state[3][pos], state[3][pos+1], state[3][pos+2]
                if x == -1 and y == 0:
                    score = ob
                else:
                    c = [' ', '#', '=', '_', '*'][ob]
                    grid[y][x] = c
    except:
        print(pos, x, y, ob)
        raise("State exception")
    print("Score:", score)
    for row in grid:
        print("".join(row))

def getInput(state):
    score = 0
    batX = state[3][2::3].index(3) * 3
    ballX = state[3][2::3].index(4) * 3
    for pos in range(0, len(state[3]), 3):
        if pos + 2 <= len(state[3]):
            x, y, ob = state[3][pos], state[3][pos+1], state[3][pos+2]
            if ob == 3:
                batX = x
            elif ob == 4:
                ballX = x
            if x == -1 and y == 0:
                score = ob
    if batX > ballX:
        state[2].append(-1)
    elif batX < ballX:
        state[2].append(1)
    else:
        state[2].append(0)

data = [int(x) for x in open("day13input.txt", "r").readline().strip().split(',')]
data.extend([0]*1000)

print("Part 1")
not_done = True
d = data[:]
state = [0, 0, [], []]    #(position, relative position, input list, outputs)
while not_done: 
    result = test(state, d)
    if result == -1 or d[state[0]] == 99:
        print('Final output:',state[3][-1])
        not_done = False

print(state[3][2::3].count(2))

print("Part 2")
not_done = True
d = data[:]
d[0] = 2
state = [0, 0, [], []]    #(position, relative position, input list, outputs)
while not_done: 
    result = test(state, d, "AUTO")
    if d[state[0]] == 99:
        print('Final output:',state[3][-1])
        not_done = False

