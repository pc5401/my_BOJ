import sys
import heapq
input = sys.stdin.readline


arr = []
N = int(input())
for n in range(N):
    x = int(input())
    if x:
        v = -x
        heapq.heappush(arr, v)
    else:
        if arr:
            v = heapq.heappop(arr)
            print(-v)
        else:
            print(0)

