import sys
input = sys.stdin.readline


def solve(T: int, numbers: list[int]) -> int:
    rtn = []

    for number in numbers:
        cnt = 0
        i = 5
        while number // i > 0:
            cnt += number // i
            i *= 5
        rtn.append(cnt)
    
    return rtn


def main():
    # 입력값
    T: int = int(input())
    numbers: list[int] = [int(input()) for _ in range(T)]

    # 풀이
    result: list[int] = solve(T, numbers)

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
