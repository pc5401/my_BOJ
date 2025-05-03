import sys
input = sys.stdin.readline

def solve(N: int, L: int, I: int) -> str:
    comb = [[0]*(L+1) for _ in range(N+1)]
    for n in range(N+1):
        comb[n][0] = 1
        for k in range(1, min(n, L)+1):
            comb[n][k] = comb[n-1][k-1] + comb[n-1][k]
    result = []
    remaining_ones = L
    idx = I
    for pos in range(N):
        rem = N - pos - 1
        cnt0 = 0

        for k in range(0, remaining_ones+1):
            if k <= rem:
                cnt0 += comb[rem][k]
        if idx <= cnt0:
            result.append('0')
        else:
            result.append('1')
            idx -= cnt0
            remaining_ones -= 1
    return "".join(result)

def main():
    # 입력
    N, L, I = map(int, input().split())
    # 풀이
    result = solve(N, L, I)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
