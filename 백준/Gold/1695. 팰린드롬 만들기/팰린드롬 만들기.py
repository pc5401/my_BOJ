import sys
input = sys.stdin.readline

def solve(N: int, A: list[int]) -> int:
    dp = [0] * N
    for i in range(N-2, -1, -1):
        prev = 0
        for j in range(i+1, N):
            temp = dp[j]
            if A[i] == A[j]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(dp[j], dp[j-1])
            prev = temp
    return dp[N-1]

def main():
    # 입력
    N = int(input().strip())
    A = list(map(int, input().split()))
    # 풀이
    result = solve(N, A)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
