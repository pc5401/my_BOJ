import sys
input = sys.stdin.readline


def solve(a: list[str], b: list[str]) -> str:
    A = [ord(w) for w in a]
    B = [ord(w) for w in b]
    lst = A + B

    lst.sort()

    return "".join([chr(lst[i]) for i in range(len(a))])


def main():
    # 입력값
    a = list(input().rstrip())
    b = list(input().rstrip())

    # 풀이
    result: str = solve(a, b)

    # 출력
    print(result)

if __name__ == "__main__":
    main()