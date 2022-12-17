T = int(input())
res = []
for t in range(T):
    c = int(input())
    q = c // 25
    d = (c - 25*q) // 10
    n = (c - 25*q - 10*d) // 5
    p = (c - 25*q - 10*d - 5*n) // 1
    res.append([q,d,n,p])

for r in res:
    print(*r)
    