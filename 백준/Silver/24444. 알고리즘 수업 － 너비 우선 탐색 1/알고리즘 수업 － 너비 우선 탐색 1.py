from collections import deque, defaultdict

graph = defaultdict(list)
N, M, R = map(int,input().split())
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)

q = deque()
q.append(R)
cnt = 1
visited[R] =cnt

while q:
    
    value = q.popleft()
    
    lst = sorted(graph[value])

    for i in lst:
        if not visited[i]:
            q.append(i)
            cnt += 1
            visited[i] = cnt

for i in visited[1:]:
    print(i)

