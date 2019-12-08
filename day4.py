import time
start = time.perf_counter()

nStart = 128392
nEnd = 643281
passwords = set()
passwords2 = set()

for i in range(nStart, nEnd + 1):
    ascending = True
    current = -1
    s = str(i)
    for x in s:
        if int(x) < current:
            ascending = False
            break
        current = int(x)
    if ascending:
        for x in range(10):
            if str(x) + str(x) in s:
                passwords.add(i)
                if str(x) + str(x) + str(x) not in s:
                    passwords2.add(i)

print(len(passwords))
print(len(passwords2))

end = time.perf_counter()
print("elapsed:", end-start,"s")
