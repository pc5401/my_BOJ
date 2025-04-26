import sys
input = sys.stdin.readline

def solve(A: list[int]) -> list[int]:
    maxA = max(A)
    freq = [0] * (maxA + 1)
    for x in A:
        freq[x] += 1
    div_cnt = [0] * (maxA + 1)
    for v in range(1, maxA + 1):
        if freq[v]:
            for m in range(v, maxA + 1, v):
                div_cnt[m] += freq[v]
    return [div_cnt[x] - 1 for x in A]

def main():
    # 입력
    N = int(input().strip())
    A = [int(input().strip()) for _ in range(N)]
    # 풀이
    result = solve(A)
    # 출력
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
