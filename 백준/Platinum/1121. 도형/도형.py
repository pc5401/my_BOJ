import sys
input = sys.stdin.readline

def solve(N, lengths, K):
    a = sorted(lengths)
    max_len = a[-1]

    DP = [[0] * (max_len + 1) for _ in range(K)]
    DP[0][0] = 1

    result = 0
    from math import comb

    for i, ai in enumerate(a):
        if i >= K - 1:
            # 전체 조합 수
            total = comb(i, K - 1)
            count_le = sum(DP[K - 1][:ai + 1])
            result += total - count_le

        for j in range(min(K - 1, i + 1), 0, -1):
            row_j = DP[j]
            prev = DP[j - 1]
            for s in range(max_len, ai - 1, -1):
                row_j[s] += prev[s - ai]

    return result

def main():
    # 입력
    N = int(input())
    lengths = list(map(int, input().split()))
    K = int(input())

    # 풀이
    result = solve(N, lengths, K)

    # 출력
    print(result)

if __name__ == "__main__":
    main()