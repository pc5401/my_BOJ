import sys
input = sys.stdin.readline

def solve(t: int, x: int, monsters: list[tuple[int,int]]) -> int:
    INF = 10**18
    min_n = INF
    for d, s in monsters:
        min_n = min(min_n, (d - 1) // s)
    if min_n == 0:
        return 0
    if t > min_n:
        picks = min_n + (t - min_n) // 2
    else:
        picks = t
    return picks * x

def main():
    # 입력
    t, x, m = map(int, input().split())
    monsters = [tuple(map(int, input().split())) for _ in range(m)]
    # 풀이
    result = solve(t, x, monsters)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
