import sys, math
input = sys.stdin.readline

def solve(points):
    points.sort(key=lambda p: p[0])
    n = len(points)
    dp = [0.0] * n
    ans = 0.0
    for i in range(n):
        xi, yi = points[i]
        best = 0.0
        for j in range(i):
            xj, yj = points[j]
            if xj < xi:
                d = math.hypot(xi - xj, yi - yj)
                candidate = dp[j] + d
                if candidate > best:
                    best = candidate
        dp[i] = best
        if dp[i] > ans:
            ans = dp[i]
    return ans

def main():
    # 입력
    N = int(input().strip())
    pts = [tuple(map(int, input().split())) for _ in range(N)]
    # 풀이
    result = solve(pts)
    # 출력
    print(f"{result:.7f}")

if __name__ == "__main__":
    main()
