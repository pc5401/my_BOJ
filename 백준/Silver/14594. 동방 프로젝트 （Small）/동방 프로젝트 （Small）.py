def cut(x, y):
    for i in range(x, y):
        lst[i] = 0

N = int(input())
M = int(input())

lst = [1 for i in range(N)]

for m in range(M):
    x, y = map(int, input().split())
    cut(x, y)

print(sum(lst))