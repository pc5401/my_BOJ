N = int(input())
l = len(str(N))
res = N
for i in range(l-1):
    v = int(str(res)[-i-1])

    if v >= 5:
        res += (10-v) * 10**i
    else:
        res -= v * 10**i
    

print(res)