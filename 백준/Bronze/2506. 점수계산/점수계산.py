import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

cnt = 0
res = 0

for i in lst:
    if i:
        cnt += 1
        res += cnt
    else:
        cnt = 0

print(res)