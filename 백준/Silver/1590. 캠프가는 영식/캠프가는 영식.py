import sys
input = sys.stdin.readline

N, T = map(int,input().split())
res = -1
for n in range(N):
    s,l,c = map(int,input().split())
    for i in range(c):
        if s >= T:
            res = min(res,s - T) if res >= 0 else s - T
            break
        s += l
print(res)

