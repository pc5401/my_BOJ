import sys
input = sys.stdin.readline

def solve(k: int, n: int) -> int:
    if k == 0:
        return 0
    max_pos = k + n
    dp = [ [0] * (max_pos + 1) for _ in range(n + 1) ]
    dp[0][k] = 1

    for t in range(n):
        for pos in range(1, max_pos + 1):
            v = dp[t][pos]
            if not v:
                continue
                
            if pos - 1 >= 1:
                dp[t+1][pos-1] += v
                
            if pos + 1 <= max_pos:
                dp[t+1][pos+1] += v
                
    return sum(dp[n][1:])

def main():
    # 입력
    k, n = map(int, input().split())
    # 풀이
    result = solve(k, n)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
