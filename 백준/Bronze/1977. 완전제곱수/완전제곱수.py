M = int(input())
N = int(input())
res = []
arr = []
for i in range(1,101):
    arr.append(i*i)

for a in arr:
    if M <= a and a <= N:
        res.append(a)
result = []

if res:
    result.append(sum(res))
    result.append(res[0])
else:
    result.append(-1)

for r in result:
    print(r)