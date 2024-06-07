import sys
input = sys.stdin.readline


def solve(N: int, trees: list[int]) -> int:
    Q = sorted(trees)

    end_day = Q.pop()
    while Q:
        end_day -= 1
        tree = Q.pop()
        if tree > end_day:
            end_day = tree

    return N + end_day + 1


def main():
    # 입력값
    N: int = int(input())
    trees: list[int] = list(map(int, input().split()))

    # 풀이
    result: list[int] = solve(N, trees)

    # 출력
    print(result)


if __name__ == "__main__":
    main()
