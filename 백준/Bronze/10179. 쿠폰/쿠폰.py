import sys
input = sys.stdin.readline


def main():
    # 입력값
    n = int(input())

    # 풀이
    result = [ round(float(input()) * 0.8, 2) for _ in range(n)]

    # 출력
    for res in result:
        print("$%.2f" % res)


if __name__ == "__main__":
    main()


