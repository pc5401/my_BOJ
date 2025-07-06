import sys
input = sys.stdin.readline
MOD = 10**9 + 7

def solve(queries: list[int]) -> list[int]:
    answers = []
    for N in queries:
        if N == 1:
            answers.append(5)
        else:
            # 4 * 5^(N-1) mod
            answers.append((4 * pow(5, N-1, MOD)) % MOD)
    return answers

def main():
    # 입력
    Q = int(input().strip())
    queries = [int(input().strip()) for _ in range(Q)]
    # 풀이
    results = solve(queries)
    # 출력
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
