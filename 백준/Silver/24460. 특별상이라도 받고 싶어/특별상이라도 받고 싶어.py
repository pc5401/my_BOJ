import sys
input = sys.stdin.readline


def solve(ai: int, aj: int, bi: int, bj: int, arr: list[int]) -> int:
    if ai == bi and aj == bj:
        return arr[ai][aj]

    mid_i = (ai + bi) // 2
    mid_j = (aj + bj) // 2

    val1 = solve(ai, aj, mid_i, mid_j, arr)
    val2 = solve(ai, mid_j + 1, mid_i, bj, arr)
    val3 = solve(mid_i + 1, aj, bi, mid_j, arr)
    val4 = solve(mid_i + 1, mid_j + 1, bi, bj, arr)

    values = sorted([val1, val2, val3, val4])
    return values[1]


def main():
    # 입력
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(0, 0, N-1, N-1, arr)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
