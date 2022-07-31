N = int(input())
res = [0] * N
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    k = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            k += 1
    res[i] = k + 1

print(*res)
