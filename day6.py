data = [x.strip().split(')') for x in open("day6input.txt", "r")] 
#data = [['COM','B'], ['B','G'], ['B','C'], ['G', 'H'], ['C','D'], ['D','I'], ['D','E'], ['E','F'], ['E','J'], ['J','K'], ['K','L']]
grav = dict()

for x in data:
    if x[0] in grav:
        grav[x[0]].append(x[1])
    else:
        grav[x[0]] = [x[1]]
    if x[1] not in grav:
        grav[x[1]] = []

def t(key, val, L):
    L.append(val)
    for x in grav[key]:
        t(x,val+','+x,L)
    return L

paths = t('COM','COM',[])
total = 0
for x in paths:
    total += len(x.split(',')) - 1

print(total)

for x in paths:
    if x[-3:]=='YOU':
        you = x.split(',')
    elif x[-3:]=='SAN':
        san = x.split(',')

mismatch = 0
for i in range(min(len(you), len(san))):
    if you[i] != san[i]:
        mismatch = i
        break

print(len(you[mismatch:]) - 1 + len(san[mismatch:]) - 1)

#Alternative version using networkx
import networkx as nx
g1 = nx.read_edgelist("day6input.txt", delimiter=")", create_using=nx.DiGraph)
print(sum(len(nx.ancestors(g1, n)) for n in g1.nodes))

g2 = nx.read_edgelist("day6input.txt", delimiter=")")
print(len(nx.shortest_path(g2, "YOU", "SAN")) - 3)
