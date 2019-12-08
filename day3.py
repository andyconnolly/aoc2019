import time
import math
start = time.perf_counter()
data = [x.strip().split(',') for x in open("day3input.txt", "r")] 

def processPath(path):
    x = 0
    y = 0
    p = [(x, y)]
    dict = {}
    t = 0
    for m in path:
        d = int(m[1:])
        if m[0] == 'R':
            for h in range(1, d+1):
                x = x + 1
                p.append((x, y))
                t = t + 1
                if (x,y) not in dict:
                    dict[(x,y)] = t
        elif m[0] == 'L':
            for h in range(1, d+1):
                x = x - 1
                p.append((x, y))
                t = t + 1
                if (x,y) not in dict:
                    dict[(x,y)] = t
        elif m[0] == 'U':
            for h in range(1, d+1):
                y = y + 1
                p.append((x, y))
                t = t + 1
                if (x,y) not in dict:
                    dict[(x,y)] = t
        elif m[0] == 'D':
            for h in range(1, d+1):
                y = y - 1
                p.append((x, y))
                t = t + 1
                if (x,y) not in dict:
                    dict[(x,y)] = t
        else:
            print("Error in input:", m)
    return p, dict

wire1, dict1 = processPath(data[0])
wire2, dict2 = processPath(data[1])

set1 = set(wire1)
set2 = set(wire2)

intersect = set1.intersection(set2)
intersect.remove((0,0))
minD = 1000000000
fewestSteps = 1000000000
for x in intersect:
    v = abs(x[0]) + abs(x[1])
    if v < minD:
        minD = v
    s = dict1[x] + dict2[x]
    if s < fewestSteps:
        fewestSteps = s

print(minD)
print(fewestSteps)

end = time.perf_counter()
print("elapsed:", end-start,"s")
