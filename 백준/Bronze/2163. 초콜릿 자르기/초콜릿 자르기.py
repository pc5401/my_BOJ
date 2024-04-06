import sys
input = sys.stdin.readline


def main():
    # 입력값
    N, M = map(int, input().split())

    # 풀이 후, 출력
    print(N*M-1)


if __name__ == "__main__":
    main()
