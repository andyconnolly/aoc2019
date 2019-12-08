data = [int(x) for x in open("day5input.txt", "r").readline().strip().split(',')]

def value(data, pos, idx):
    mode = str(data[pos])[:-2].zfill(3)
    return data[data[pos+idx]] if (mode[-idx] == '0') else data[pos+idx]

def test(inp, data):
    pos = 0
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
            data[data[pos+1]] = inp
            pos += 2
        elif code == '04':
            output = value(data, pos, 1)
            print(output)
            pos += 2
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
    return output

d = data[:]
assert test(1, d) == 6731945
d = data[:]
assert test(5, d) == 9571668
