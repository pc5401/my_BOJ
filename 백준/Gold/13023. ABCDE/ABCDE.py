import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
dct = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    dct[a].append(b)
    dct[b].append(a)

# 깊이가 4 인 DFS 찾기

lst = []
res = 0
def DFS(node ,lst):
    global res

    lst.append(node)
    if len(lst) > 4:
        res = 1
        print(1)
        exit()
        return

    if dct[node]:
        for i in dct[node]:
            if not i in lst:
                # print(lst)
                DFS(i, lst[:])
for i in dct:
    DFS(i ,lst[:])

print(res)