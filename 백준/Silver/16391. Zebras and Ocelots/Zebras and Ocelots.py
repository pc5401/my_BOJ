import sys
input = sys.stdin.readline


def solve(data: list[str]) -> int:
    return int("".join(data), 2)

if __name__ == '__main__':
    # 입력값
    N = int(input())
    data = [ '0' if input().rstrip() == 'Z' else '1' for _ in range(N)]
    
    # 풀이
    result = solve(data)

    # 출력
    print(result)
    