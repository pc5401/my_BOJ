n, x = map(int,input().split())
a = list(map(int,input().split()))
res = []

for i in a:
    if x > i:
        res.append(i)

print(*res)