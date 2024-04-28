import sys
input = sys.stdin.readline


def main():
    # 입력값
    n, m = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    # 풀이
    result = list(A - B)
    # 출력
    result.sort()
    print(len(result))
    if result:
        print(*result)


if __name__ == "__main__":
    main()