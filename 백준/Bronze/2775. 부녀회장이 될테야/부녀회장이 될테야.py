T = int(input())

arr = [[i for i in range(1, 15)] if j == 0 else [0 for i in range(1, 15)] for j in range(15)]

for i in range(1, 15):
    sum = 0
    for j in range(14):
        sum += arr[i-1][j]
        arr[i][j] += sum

for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])