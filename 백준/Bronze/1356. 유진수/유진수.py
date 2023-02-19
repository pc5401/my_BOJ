def cal(V):
    res = 1
    for v in V:
        res *= int(v)
    return res


n = input()
l = len(n)
res = 'NO'
for i in range(l-1):
    a = n[0:i+1]
    b = n[i+1:]
    if cal(a) == cal(b):
        res = 'YES'
        break
print(res)

