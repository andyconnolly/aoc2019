data = open("day8input.txt", "r").read()
layer_size = 25 * 6
layers = [data[i:i+layer_size] for i in range(0, len(data), layer_size)]

min_layer = None
min_count = 1000000000
for i in range(len(layers)):
    count_zeros = layers[i].count('0')
    if count_zeros < min_count:
        min_count = count_zeros
        min_layer = i

print("Layer:", min_layer, "- Zeros:", min_count, "- Ones x Twos:", layers[min_layer].count('1') * layers[min_layer].count('2'))

composite = list(layers[0])
for i in range(1, len(layers)):
    for j in range(len(layers[i])):
        if composite[j] == '2':
            composite[j] = layers[i][j]

comp = [composite[i:i+25] for i in range(0, len(composite), 25)]
for row in comp:
    print(''.join(row).replace('1','#').replace('0',' '))
