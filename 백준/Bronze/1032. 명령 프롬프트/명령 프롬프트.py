N = int(input())
lst = [list(input()) for _ in range(N)]
M = len(lst[0])
res = lst[0][:]

if N < 2:
    if M == 1:
        print(*lst[0])
        quit()
    else:
        print("".join(res))
        quit()

for j in range(M):
    for i in range(1,N):
        if lst[i][j] != lst[i-1][j]:
            res[j] = '?'


print("".join(res))
