from collections import deque

N, K = map(int, input().split())  # 0~100,000

visit = [[0,0] for _ in range(100001)]
visit[N] = [1, N]
que = deque()
que.append(N)

while que:
    v = que.popleft()
    if v*2 < 100001 and visit[v*2] == [0,0]:
        visit[v*2][0] = visit[v][0] + 1
        visit[v*2][1] = v
        que.append(v*2)
        if v*2 == K:
            break

    if v+1 < 100001 and visit[v + 1] == [0,0]:
        visit[v+1][0] = visit[v][0] + 1
        visit[v+1][1] = v
        que.append(v+1)
        if v+1 == K:
            break
    
    if 0 <= v-1 and visit[v - 1] == [0,0]:
        visit[v-1][0] = visit[v][0] + 1
        visit[v-1][1] = v
        que.append(v-1)
        if v-1 == K:
            break
    

result = visit[K][0]
res = [K]
k = visit[K][1]

while k != N:
    res.append(k)
    k = visit[k][1]
    
if res[-1] != N:
    res.append(N)

print(result-1)
print(*res[::-1])