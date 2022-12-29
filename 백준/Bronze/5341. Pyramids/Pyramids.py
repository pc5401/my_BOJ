flag = True
res = []
while flag:
    v = int(input())
    if v:
        res.append(v*(v+1)//2)
    else:
        break
for r in res:
    print(r)