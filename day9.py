def value(data, state, idx):
    mode = str(data[state[0]])[:-2].zfill(3)[-idx]
    return data[state[0]+idx] if (mode == '0') else (state[0]+idx if (mode == '1') else data[state[0]+idx] + state[1])

def test(state, data):
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
            data[value(data, state, 1)] = state[2].pop(0)
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

data = [int(x) for x in open("day9input.txt", "r").readline().strip().split(',')]
data.extend([0]*1000)

for i in range(1,3):
    not_done = True
    d = data[:]
    state = [0, 0, [i], []]    #(position, relative position, input list, outputs)
    while not_done: 
        result = test(state, d)
        print(state)
        if result == -1 or d[state[0]] == 99:
            print('Final output:',state[3][-1])
            not_done = False

