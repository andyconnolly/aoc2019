import itertools as it
#data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0] #43210, [4, 3, 2, 1, 0]
#data = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0] #54321, [0,1,2,3,4]
#data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0] #65210, [1,0,4,3,2]

data = [int(x) for x in open("day7input.txt", "r").readline().strip().split(',')]

def value(data, pos, idx):
    mode = str(data[pos])[:-2].zfill(3)
    return data[data[pos+idx]] if (mode[-idx] == '0') else data[pos+idx]

def test(pos, inp, data):
    output = -1
    while data[pos] != 99:
        if data[pos] < 10:
            code = str(data[pos]).zfill(2)
        else:
            code = str(data[pos])[-2:]
        if code == '01':
            data[data[pos+3]] = value(data, pos, 1) + value(data, pos, 2)
            pos += 4
        elif code == '02':
            data[data[pos+3]] = value(data, pos, 1) * value(data, pos, 2)
            pos += 4
        elif code == '03':
            data[data[pos+1]] = inp.pop(0)
            pos += 2
        elif code == '04':
            output = value(data, pos, 1)
            #print(output)
            pos += 2
            return output, pos
        elif code == '05':
            pos = (pos + 3) if (value(data, pos, 1) == 0) else value(data, pos, 2)
        elif code == '06':
            pos = (pos + 3) if (value(data, pos, 1) != 0) else value(data, pos, 2)
        elif code == '07':
            data[data[pos+3]] = 1 if (value(data, pos, 1) < value(data, pos, 2)) else 0
            pos += 4
        elif code == '08':
            data[data[pos+3]] = 1 if (value(data, pos, 1) == value(data, pos, 2)) else 0
            pos += 4
        else:
            print("error - found code",code,"at position",pos,"- data is:",data[pos])
            break
    return output, -1

highest = 0
permutation = None

for p in it.permutations([0,1,2,3,4], 5):
    d = data[:]
    result = 0
    for i in range(5):
        result = test(0, [p[i], result], d)[0]
    if result > highest:
        highest = result
        permutation = p

print(highest, permutation)

#data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5] #139629729 [9,8,7,6,5]
#data = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10] #18216 [9,7,8,5,6]
data = [int(x) for x in open("day7input.txt", "r").readline().strip().split(',')]

highest = 0
permutation = None
for p in it.permutations([5,6,7,8,9], 5):
    result = 0
    amps = [data[:], data[:], data[:], data[:], data[:]]
    positions = [0, 0, 0, 0, 0]
    inputs = [[p[0], 0], [p[1]], [p[2]], [p[3]], [p[4]]]
    last_E_value = 0
    notFound = True
    
    while notFound:
        for i in range(5):
            result = test(positions[i], inputs[i], amps[i])
            if i == 4:
                last_E_value = result[0]
            inputs[(i+1)%5].append(result[0])
            positions[i] = result[1]
            if result[1] == -1:
                if last_E_value > highest:
                    highest = last_E_value
                    permutation = p
                notFound = False
                break

print(highest, permutation)
