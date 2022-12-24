import sys
input = sys.stdin.readline


n = int(input())

res = 1
for i in range(n):
    v = int(input())
    res += v

print(res - n)
