import sys
input = sys.stdin.readline


def solve(N: int, lst: list[int]) -> int:
    return sum(lst) - max(lst)

def main():
    # 입력
    N = int(input())
    lst = list(map(int, input().split()))

    # 풀이
    result = solve(N, lst)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
