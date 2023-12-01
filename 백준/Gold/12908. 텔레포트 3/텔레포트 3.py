import sys
input = sys.stdin.readline

def cal_len(idx: int):
    x, y = arr[idx]
    for i in range(8):
        a, b = arr[i]
        dp[idx][i] = abs(x-a) + abs(y-b)


if __name__ == "__main__":
    xs, ys = map(int, input().split())
    xe, ye = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(3)]
    dp = [[0]*8 for _ in range(8)]
    arr = [[xs, ys]]
    for a, b, c, d in lst:
        arr.append([a,b])
        arr.append([c,d])
    arr.append([xe, ye])
    
    for i in range(8):
        cal_len(i)

    for i in range(1, 6, 2):
        dp[i][i+1] = 10
        dp[i+1][i] = 10

    for k in range(8):
        for i in range(8):
            for j in range(8):
                if i == j:
                    continue
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    
    print(dp[0][-1])