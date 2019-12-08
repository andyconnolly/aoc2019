#data = [1,0,0,0,99]		#becomes 2,0,0,0,99 (1 + 1 = 2).
#data = [2,3,0,3,99] 		#becomes 2,3,0,6,99 (3 * 2 = 6).
#data = [2,4,4,5,99,0] 		#becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
#data = [1,1,1,4,99,5,6,0,99]	#becomes 30,1,1,4,2,5,6,0,99.

#part 1
data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0]
data[1] = 12
data[2] = 2

pos = 0
while data[pos]!=99:
    if data[pos] == 1:
        data[data[pos+3]] = data[data[pos+1]] + data[data[pos+2]]
    elif data[pos] == 2:
        data[data[pos+3]] = data[data[pos+1]] * data[data[pos+2]]
    else:
        print("error - found",data[pos],"at position",pos)
    pos +=4

print(data)

#part 2
found = False
for noun in range(100):
    #print(noun)
    for verb in range(100):
        #print("  ",verb,end= " ")
        data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0]
        data[1] = noun
        data[2] = verb
        pos = 0
        while data[pos]!=99:
            if data[pos] == 1:
                data[data[pos+3]] = data[data[pos+1]] + data[data[pos+2]]
            elif data[pos] == 2:
                data[data[pos+3]] = data[data[pos+1]] * data[data[pos+2]]
            else:
                print("error - found",data[pos],"at position",pos)
            pos +=4
        #print(data[0])
        if data[0] == 19690720:
            print("noun:",noun," verb:",verb," result:",100*noun+verb)
            found = True
            break
    if found:
        break
