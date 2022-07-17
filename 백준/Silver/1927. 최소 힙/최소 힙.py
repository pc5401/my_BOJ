import sys
import heapq
input = sys.stdin.readline


arr = []
N = int(input())
for n in range(N):
    x = int(input())
    if x:
        heapq.heappush(arr, x)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
