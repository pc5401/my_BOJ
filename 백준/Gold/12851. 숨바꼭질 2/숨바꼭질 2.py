from collections import deque

N, K = map(int, input().split())  # 0~100,000

if N == K:
    print(0)
    print(1)
    exit()

visit = [1e9] * 100001
visit[N] = 1
que = deque()
que.append(N)

cnt = 0

flag = 0
while que:

    v = que.popleft()

    for d in [v+1, v-1, v*2]:

        if 0 <= d < 100001 and visit[d] > visit[v]:
            visit[d] = visit[v] + 1
            que.append(d)

        if d == K and visit[K] > 0 and visit[K] == visit[v] + 1:
            cnt += 1
    

res = visit[K]
# print(visit[:100])
print(res-1)
print(cnt)
