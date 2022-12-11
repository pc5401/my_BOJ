n = int(input())

res = []
for i in range(1,n+1):
    v = ' '*(n-i) + '*'*(i*2-1)
    res.append(v)

for r in res:
    print(r)

lst = res[::-1]
for l in lst[1:]:
    print(l)