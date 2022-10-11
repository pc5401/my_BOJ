from collections import defaultdict

N = int(input())
x, y = map(int,input().split())
M = int(input())

family = defaultdict(list)

for _ in range(M):
    a,b = map(int ,input().split())
    family[a].append(b)
    family[b].append(a)

stc = [[x,0]]
visited = [x]
res = -1
cnt = 0

while stc:
    v = stc.pop()

    if v[0] == y:
        cnt = v[1]
        break

    for i in family[v[0]]:
        if not i in visited:
            stc.append([i, v[1]+1])
            visited.append(i)

print(cnt if cnt else res)

