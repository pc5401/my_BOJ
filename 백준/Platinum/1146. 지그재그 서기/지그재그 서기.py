import sys
input = sys.stdin.readline

MOD = 10**6

def solve(N: int) -> int:
    if N == 1:
        return 1
    up = [0, 1]
    down = [0, 1]
    for n in range(2, N+1):
        ps_down = [0] * n
        ps_up = [0] * n
        for i in range(1, n):
            ps_down[i] = (ps_down[i-1] + down[i]) % MOD
            ps_up[i]   = (ps_up[i-1]   + up[i])   % MOD
        new_up = [0] * (n+1)
        new_down = [0] * (n+1)
        for k in range(1, n+1):
            new_up[k] = ps_down[k-1]
            new_down[k] = (ps_up[n-1] - ps_up[k-1]) % MOD
        up, down = new_up, new_down
    total = (sum(up[1:]) + sum(down[1:])) % MOD
    return total

def main():
    # 입력
    N = int(input())
    # 풀이
    result = solve(N)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
