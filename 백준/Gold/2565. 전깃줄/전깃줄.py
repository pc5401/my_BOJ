if __name__ == '__main__':
    AB = []
    N = int(input())
    for i in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort(key=lambda x : x[0])
    dp = [1] * N
    for i in range(1,N):
        for j in range(0,i):
            if AB[i][1] > AB[j][1] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    res = N -max(dp)
    print(res)