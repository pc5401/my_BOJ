N = int(input())
data = dict()
lst = []

for i in range(N):
    v = input()
    if v in data:
        data[v] += 1
    else:
        data[v] = 1
        lst.append(v)

res = []
maxV = 0

for j in lst:
    if data[j] == maxV and res:
        res.append(j)
        
    elif data[j] > maxV:
        res = []
        res.append(j)
        maxV = data[j]

if len(res) > 1:
    res.sort()

print(res[0])
