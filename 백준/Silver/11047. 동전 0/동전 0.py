import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

res = 0
k = K
for a in A[::-1]:
    x, y = divmod(k, a)
    res += x
    k -= x*a if x > 0 else 0
print(res)
