import heapq

n = int(input())
v = int(input())
hq = []
for i in range(n-1):
    item = int(input())
    heapq.heappush(hq, -item)

cnt = 0
try:
    while v <= abs(hq[0]):
        
        h = heapq.heappop(hq)
        heapq.heappush(hq, h+1)
        v += 1
        cnt += 1
except IndexError:
    cnt = 0

print(cnt)