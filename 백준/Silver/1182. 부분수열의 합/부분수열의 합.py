def cal(idx:list,n:int):
    global res

    v = 0
    for i in idx:
        v += lst[i]

    if v == S:
        res += 1

    for i in range(n,N):
        if not i in idx:
            idx.append(i)
            cal(idx,i)
            idx.pop()


N,S = map(int,input().split())
lst = list(map(int,input().split()))
res = 0

for i in range(N):
    cal([i],i)

print(res)