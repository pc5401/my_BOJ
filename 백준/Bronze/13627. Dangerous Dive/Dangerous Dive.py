import sys
input = sys.stdin.readline

N, R = map(int,input().split())
lst = list(map(int,input().split())) 
res = [0] * (N)

for i in lst:
    if res[i-1]: continue
    res[i-1] = 1
resulst = []
for i,v in enumerate(res,start=1):
    if not v:
        resulst.append(i)

print(*resulst if resulst else '*')

