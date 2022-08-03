def func(i, j, n):
    value = arr[i][j]

    for y in range(i, i + n):
        for x in range(j, j +n):
            if arr[y][x] != value:  # 재귀로 
                func(i, j, n // 3)
                func(i, j + n // 3, n // 3)
                func(i, j + n // 3 * 2, n // 3)

                func(i + n // 3, j, n // 3)
                func(i + n // 3, j + n // 3, n // 3)
                func(i + n // 3, j + n // 3 * 2, n // 3)

                func(i + n // 3 * 2, j, n // 3)
                func(i + n // 3 * 2, j + n // 3, n // 3)
                func(i + n // 3 * 2, j + n // 3 * 2, n // 3)
                return

    res[value] += 1
    return True


N = int(input())
arr = [list(map(int, input().split()))for n in range(N)]
res = {0:0, 1:0, -1:0}

func(0,0,N)

print(res[-1])
print(res[0])
print(res[1])