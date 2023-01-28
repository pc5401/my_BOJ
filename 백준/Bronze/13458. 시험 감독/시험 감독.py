import math, sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B, C =map(int,input().split())

cnt = 0
for i in range(N):
    a = A[i]
    a -= B
    cnt += 1
    if a > 0:
        cnt += math.ceil(a / C)

print(cnt)