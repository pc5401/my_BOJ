from collections import defaultdict, deque


c = int(input()) # 컴퓨터 수
lst = [0]*(c+1)
n = int(input())
data = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

que = deque()

que.append(1)
lst[1] = 1

while que:
    v = que.popleft()
    lst[v] = 1

    for i in data[v]:
        if not lst[i]:
            que.append(i)

print(lst.count(1) - 1)