import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

l, r = 0,0
# 왼쪽
maxV = 0
for i in lst:
    if i > maxV:
        l += 1
        maxV = i
    elif i <= maxV:
        continue
# 오른쪽
maxV = 0
for i in lst[::-1]:
    if i > maxV:
        r += 1
        maxV = i
    elif i <= maxV:
        continue
print(l)
print(r)