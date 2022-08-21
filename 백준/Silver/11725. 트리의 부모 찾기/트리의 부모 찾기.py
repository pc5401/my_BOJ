from collections import defaultdict

N = int(input())
tree = defaultdict(list)
res = [0] * (N)

for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

stack = [1]
res[0] = 1
while stack:
    v = stack.pop()
    for i in tree[v]:
        if res[i-1] == 0:
            res[i-1] = v
            stack.append(i)

for r in res[1:]:
    print(r)