import sys
input = sys.stdin.readline


def solve(lst: list[str]) -> int:
    lst = sorted(lst, reverse=True)
    a = int("".join(lst[:-1]))
    b = int(lst[-1])
    return a+b


def main():
    # 입력값
    N = int(input())
    result = []
    for _ in range(N): # 풀이
        input()
        result.append(solve(list(input().rstrip())))

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()