import sys
input = sys.stdin.readline


def solve(a: int, b: int) -> int:
    rtn = 0

    num = a
    while True:

        if num == b:
            return rtn
        elif num > b and num % 2 == 0:
            num //= 2
        elif num < b:
            return rtn + (b-num)
        else:
            num += 1

        rtn += 1

def main():
    # 입력값
    a, b = map(int, input().split())
    a: int
    b: int
    # 풀이
    result: int = solve(a, b)
    # 출력
    print(result)


if __name__ == "__main__":
    main()