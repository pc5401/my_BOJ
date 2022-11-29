N = int(input())
inpu_lst = []
for _ in range(N):
    inpu_lst.append(input())

set_lst = list(set(inpu_lst))

res = set_lst[:]
res.sort()
res.sort(key=len)
for r in res:
    print(r)