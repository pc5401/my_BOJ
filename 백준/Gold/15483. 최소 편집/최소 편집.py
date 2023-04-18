import sys
input = sys.stdin.readline

def res(A,B):
    A_len = len(A)
    B_len = len(B)
    dp = [[0]*(B_len+1) for _ in range(A_len+1)]

    # dp 행렬 초기화
    for i in range(A_len):
        dp[i][0] = i
    for i in range(B_len):
        dp[0][i] = i

    # 레벤슈타인 거리 계산
    for i in range(1, A_len+1):
        for j in range(1, B_len+1):
            if A[i-1] == B[j-1]: # 대체X
                dp[i][j] = dp[i-1][j-1]
            else: # 순서대로 삽입, 삭제, 대체
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1 # 그리고 연산 + 1
    
    return dp[-1][-1]


if __name__ == "__main__":
    a = input()
    b = input()
    print(res(a,b))
