import heapq
import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x = int(input())
    heapq.heappush(lst, x)

res = 0

while len(lst) > 1:

    v1 = heapq.heappop(lst)
    v2 = heapq.heappop(lst)

    v = v1 + v2
    res += v
    heapq.heappush(lst, v)

print(res)