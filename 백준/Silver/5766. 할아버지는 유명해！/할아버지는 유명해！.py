import sys
input = sys.stdin.readline

def solve(N, M, rankings):
    freq: dict[int, int] = {}
    for week in rankings:
        for player in week:
            freq[player] = freq.get(player, 0) + 1

    max_point = max(freq.values())
    second_point = max(v for v in freq.values() if v < max_point)

    result = [p for p, v in freq.items() if v == second_point]
    result.sort()
    return result

def main():
    # 입력
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        rankings = [list(map(int, input().split())) for _ in range(N)]

        # 풀이
        result = solve(N, M, rankings)

        # 출력
        print(*result)

if __name__ == "__main__":
    main()
