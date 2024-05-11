import re
import sys
input = sys.stdin.readline


def solve(N: int, data: list[str]) -> list[int]:
    return sorted([int(num) for d in data for num in re.split("[a-z]+", d) if num])


def main():
    # 입력값
    N = int(input())
    data: list[tuple[str]] = [input().rstrip() for _ in range(N)]

    # 풀이
    result: list[int] = solve(N, data)
    
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()

