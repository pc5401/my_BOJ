from collections import defaultdict, deque

graph = defaultdict(list)
N, M, V = map(int, input().split())
for m in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS
stack = deque([V])
DFS = [V]

while stack:

    v = stack[-1]
    lstV = sorted(graph[v])

    for i in lstV:
        if not i in DFS:
            stack.append(i)
            DFS.append(i)
            break
    else:
        stack.pop()

# BFS
queue = deque([V])
BFS = [V]

while queue:

    v = queue.popleft()
    lstV = sorted(graph[v])

    for i in lstV:
        if not i in BFS:
            queue.append(i)
            BFS.append(i)

print(*DFS)
print(*BFS)