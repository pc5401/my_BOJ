N, M = map(int, input().split())

lst_1 = []
lst_2 = []

for i in range(N):
    lst = list(map(int, input().split()))
    lst_1.append(lst)

for i in range(N):
    lst = list(map(int, input().split()))
    lst_2.append(lst)

res = [0] * M
for i in range(N):
    for j in range(M):
        res[j] = lst_1[i][j] + lst_2[i][j]
    print(*res)