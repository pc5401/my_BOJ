from collections import deque

N, K = map(int, input().split())  # 0~100,000

visit = [0] * 100001
visit[N] = 1
que = deque()
que.append(N)

while que:
    v = que.popleft()

    if v*2 < 100001 and visit[v*2] == 0:
        visit[v*2] = visit[v]
        que.appendleft(v*2)
        if v*2 == K:
            break

    if v+1 < 100001 and visit[v + 1] == 0:
        visit[v+1] = visit[v] + 1
        que.append(v+1)
        if v+1 == K:
            break
    
    if 0 <= v-1 and visit[v - 1] == 0:
        visit[v-1] = visit[v] + 1
        que.append(v-1)
        if v-1 == K:
            break
    
    if visit[K]:
        break

res = visit[K]
# print(visit[0:100])
print(res-1)
