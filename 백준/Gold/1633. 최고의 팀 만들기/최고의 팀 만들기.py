import sys

INF_NEG = -10**18

def solve(pairs):
    dp = [[INF_NEG]*16 for _ in range(16)]
    dp[0][0] = 0
    for w, b in pairs:
        new = [row[:] for row in dp]
        for j in range(16):
            for k in range(16):
                if dp[j][k] == INF_NEG:
                    continue
                if j < 15:
                    if new[j+1][k] < dp[j][k] + w:
                        new[j+1][k] = dp[j][k] + w
                if k < 15:
                    if new[j][k+1] < dp[j][k] + b:
                        new[j][k+1] = dp[j][k] + b
        dp = new
    return dp[15][15]

def main():
    data = sys.stdin.read().strip().split()
    # 입력
    pairs = [(int(data[i]), int(data[i+1])) for i in range(0, len(data), 2)]
    # 풀이
    ans = solve(pairs)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
