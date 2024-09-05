import sys
input = sys.stdin.readline


def solve(N: int,B: int, H: list[int]) -> int:
    cows = sorted(H)
    rtn = 0
    height = 0

    while height < B:
        cow = cows.pop()
        height += cow
        rtn += 1
    
    return rtn


def main():
    # 입력값
    N, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    
    # 풀이
    result = solve(N, B, H)

    # 출력
    print(result)


if __name__ == "__main__":
    main()


