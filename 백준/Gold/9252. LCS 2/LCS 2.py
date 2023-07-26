import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A = input().rstrip()
    B = input().rstrip()

    n = len(A)
    m = len(B)
    dp = [[0] * (n+1)  for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1,n+1):
            if A[j-1] == B[i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    res = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else: 
            res = A[j-1] + res
            i -= 1
            j -= 1

    print(dp[-1][-1])
    print(res)
