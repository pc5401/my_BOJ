import sys
input = sys.stdin.readline


P,K = map(int,input().split())

sosu = []
lst = [1] * (K+1)
lst[0], lst[1] = 0, 0
for k in range(2,K+1):
    if lst[k]:
        sosu.append(k)
        for i in range(k,K+1,k):
            lst[k] = 0
res = 'GOOD'
r = 0
for s in sosu:
    v = P % s
    if v == 0 and s < K:
        res = 'BAD'
        r = s
        break
print(res, r) if r else print(res)
