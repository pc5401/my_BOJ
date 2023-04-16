N, M = map(int,input().split())
p = [0,0]
arr = [[0]*N for i in range(M)]
i,j,d = 0,0,0
flag = 0
delta = [[0,1],[1,0],[0,-1],[-1,0]]
while True:

    if 0 <= i < M and 0 <= j < N and not arr[i][j]:
        arr[i][j] = 1
        flag = 0

    elif flag == 1:
        i = i - delta[d][0]
        j = j - delta[d][1]
        break

    else:
        i = i - delta[d][0]
        j = j - delta[d][1]
        d = (d + 1) % 4
        flag = 1

    i = i + delta[d][0]
    j = j + delta[d][1]

print(j,i)