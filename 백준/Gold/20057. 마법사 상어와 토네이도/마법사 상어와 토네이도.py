from pprint import pprint
delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def tornado(i, j, di):  # 방향 d :좌하우상 0,1,2,3
    # 상하 : i + d*2, 좌우 j + d*2 -> 5%
    if arr[i][j]:  # 모래가 있을 때, 0이면 pass
        total = 0
        d = delta[di]
        #  5%의 경우
        arr[i + d[0] * 2][j + d[1] * 2] += int(arr[i][j] * 0.05)
        total += int(arr[i][j] * 0.05)
        #  10%의 경우
        arr[i + d[0] + 1 * d[1]][j + d[1] + 1 * d[0]] += int(arr[i][j] * 0.1)
        total += int(arr[i][j] * 0.1)
        arr[i + d[0] - 1 * d[1]][j + d[1] - 1 * d[0]] += int(arr[i][j] * 0.1)
        total += int(arr[i][j] * 0.1)
        #  7%의 경우
        arr[i + d[1]][j + d[0]] += int(arr[i][j] * 0.07)
        total += int(arr[i][j] * 0.07)
        arr[i - d[1]][j - d[0]] += int(arr[i][j] * 0.07)
        total += int(arr[i][j] * 0.07)
        #  2%의 경우
        arr[i + 2 * d[1]][j + 2 * d[0]] += int(arr[i][j] * 0.02)
        total += int(arr[i][j] * 0.02)
        arr[i - 2 * d[1]][j - 2 * d[0]] += int(arr[i][j] * 0.02)
        total += int(arr[i][j] * 0.02)
        #  1%의 경우
        arr[i - d[0] + 1 * d[1]][j - d[1] + 1 * d[0]] += int(arr[i][j] * 0.01)
        total += int(arr[i][j] * 0.01)
        arr[i - d[0] - 1 * d[1]][j - d[1] - 1 * d[0]] += int(arr[i][j] * 0.01)
        total += int(arr[i][j] * 0.01)
        #  a(알파) 와 y 처리
        arr[i + d[0]][j + d[1]] = arr[i + d[0]][j + d[1]] + (arr[i][j] - total)
        arr[i][j] = 0

    return


n = int(input())
arr = [[0]*(n+4) for _ in range(2)]
lst = [[0, 0] + list(map(int, input().split())) + [0, 0] for _ in range(n)]
arr.extend(lst)
arr.extend([[0]*(n+4) for _ in range(2)])

r = n // 2 + 2  # 가운데 좌표
c = n // 2 + 2

# 좌하우상 0,1,2,3
delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
di = 0
go = 2

while 1:
    if r == 2 and c == 2:
        break

    goN = go // 2

    for k in range(goN):
        ni = delta[di][0]
        nj = delta[di][1]

        r += ni
        c += nj

        tornado(r, c, di)
        # pprint(arr)

        if r == 2 and c == 2:
            break

    di = (di + 1) % 4
    go += 1

# 밖으로 나간 모래를 구하기 위해 추가한 행과 열을 중복 없이 값을 더한다.
# 이건 뭐.... 참 무식하게도 더한다.
row_sum = sum(arr[0]) + sum(arr[1]) + sum(arr[n+2]) + sum(arr[n+3])
col_sum = 0
for i in range(2, n+2):
    col_sum += arr[i][0]
    col_sum += arr[i][1]
    col_sum += arr[i][n+2]
    col_sum += arr[i][n+3]

result = row_sum + col_sum

print(result)