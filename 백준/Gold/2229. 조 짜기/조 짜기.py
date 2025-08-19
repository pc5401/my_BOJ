import sys
input = sys.stdin.readline

def solve(N, A):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        mx = mn = A[i - 1]
        best = 0
        for j in range(i - 1, -1, -1):
            if A[j] > mx:
                mx = A[j]
            if A[j] < mn:
                mn = A[j]
            val = dp[j] + (mx - mn)
            if val > best:
                best = val
        dp[i] = best
    return dp[N]

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
