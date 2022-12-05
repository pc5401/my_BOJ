from collections import deque


N = int(input())
lst = list(map(int,input().split()))
A,B = map(int,input().split())
a,b = A - 1, B - 1
res = -1

visit = [0] * N

q = deque()

q.append(a)

while q:

    v = q.popleft()
    num = lst[v]
    cnt = visit[v]

    if v == b:
        res = cnt
        break

    for i in range(v, N, num):
        if visit[i]:
            continue

        visit[i] = cnt + 1
        q.append(i)

    for j in range(v,-1,-num):
        if visit[j]:
            continue

        visit[j] = cnt + 1
        q.append(j)

print(res)