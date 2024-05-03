import sys
input = sys.stdin.readline


def solve(N: int, A: int) -> int:
    dp = [1] * N
    
    for i in range(1, N):
        if A[i] > A[i-1]:
            dp[i] += dp[i-1]
        
    return sum(dp)


def main():
    # 입력값
    N: int = int(input())
    A: list[int] = list(map(int, input().split()))
    # 풀이
    result = solve(N, A)
    # 출력
    print(result)

if __name__ == "__main__":
    main()

