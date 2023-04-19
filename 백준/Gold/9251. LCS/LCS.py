import sys
input = sys.stdin.readline

def res(A,B):
    A_len = len(A)
    B_len = len(B)
    dp = [[0]*(B_len+1) for _ in range(A_len+1)]


    # LCS 계산
    for i in range(1, A_len+1):
        for j in range(1, B_len+1):
            if A[i-1] == B[j-1]: # 알파벳 동일
                dp[i][j] = dp[i-1][j-1] + 1
            else: # 두 문자 중 가장 긴(큰)걸 선택
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

    return dp[-1][-1]


if __name__ == "__main__":
    a = input().rstrip()
    b = input().rstrip()
    print(res(a,b))
