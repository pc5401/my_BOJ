import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A = input().rstrip()
    B = input().rstrip()
    C = input().rstrip()

    n = len(A)
    m = len(B)
    l = len(C)
    dp = [[[0] * (l+1)  for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1,m+1):
            for k in range(1, l+1):

                if A[i-1] == B[j-1] == C[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])

    print(dp[-1][-1][-1])