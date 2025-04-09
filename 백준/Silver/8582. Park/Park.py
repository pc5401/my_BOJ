import sys
input = sys.stdin.readline

def solve(n: int, w: list[int]) -> list[tuple[int, int]]:
    dp = [0] * n
    dp[0] = w[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1], w[i-1])
    dp2 = [0] * n
    dp2[n-1] = w[n-1]
    for i in range(n-2, -1, -1):
        dp2[i] = max(dp2[i+1], w[i+1])
    dp_ans = []
    for i in range(n):
        a = dp[i] if i > 0 and dp[i] > w[i] else w[i]
        b = dp2[i] if i < n-1 and dp2[i] > w[i] else w[i]
        dp_ans.append((a, b))
    return dp_ans

def main():
    # 입력
    n = int(input().strip())
    w = [int(input().strip()) for _ in range(n)]
    
    # 풀이
    result = solve(n, w)
    
    # 출력
    for a, b in result:
        print(a, b)

if __name__ == "__main__":
    main()
