import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = defaultdict(list)

for _ in range(m):
    x, y = map(int,input().split())
    lst[x].append(y)
    lst[y].append(x)

visit = [0] * (n+1)
visit[1] = 1
sck = deque()
sck.append(1)
cnt = -1

while sck:
    v = sck.popleft()

    if visit[v] > 3:
        continue

    cnt += 1

    for i in lst[v]:
        if visit[i] == 0:
            visit[i] = visit[v] + 1
            sck.append(i)

print(cnt)