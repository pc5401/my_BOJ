import sys
input = sys.stdin.readline


def solve(N: int, load_data: list[list[int]]) -> list[int]:
    start = load_data[0][1]
    D, V = 0, start

    for i in range(1, N):
        D += load_data[i-1][0]
        V += load_data[i][1]
        start = max(start, V-D)
    return start

def main():
    # 입력값
    N = int(input())
    load_data = [list(map(int, input().split())) for _ in range(N)]

    # 풀이
    result: list[int] = solve(N, load_data)

    # 출력
    print(result)


if __name__ == "__main__":
    main()