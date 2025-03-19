import sys
input = sys.stdin.readline

def solve(a: int, b: int, d: int, N: int) -> int:
    mod = 1000
    F = [0] * (N + 1)
    S = [0] * (N + 1)
    F[0] = 1
    S[0] = 1
    for n in range(1, N + 1):
        if n < a:
            F[n] = 0
        else:
            lower = n - (b - 1)
            upper = n - a
            if lower < 0:
                lower = 0
            prev = S[lower - 1] if lower > 0 else 0
            F[n] = (S[upper] - prev) % mod if upper >= 0 else 0
        S[n] = (S[n-1] + F[n]) % mod
    start_idx = N - d + 1
    if start_idx < 0:
        start_idx = 0
    result = (S[N] - (S[start_idx - 1] if start_idx > 0 else 0)) % mod
    return result

def main():
    # 입력
    a, b, d, N = map(int, input().split())
    
    # 풀이
    result = solve(a, b, d, N)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
