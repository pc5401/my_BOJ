chess = [1,1,2,2,2,8]
lst = list(map(int, input().split()))
res = [0]*6
for i in range(6):
    res[i] = chess[i] - lst[i]

print(*res)