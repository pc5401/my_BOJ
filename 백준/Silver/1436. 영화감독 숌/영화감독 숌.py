N = int(input())
res = []

value = '666'
while len(res) < 10001:
    for v in range(2, len(value)):
        intV = int(value)
        if value[v] == '6' == value[v-1] == value[v-2]:
            res.append(intV)
            break
    intV += 1
    value = str(intV)

print(res[N-1])



