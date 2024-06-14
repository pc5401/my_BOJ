import sys
input = sys.stdin.readline


def main():
    # 입력값
    A, B, C = map(int, input().split())
    # 풀이
    day  = {i for i in range(A, B)}
    result = 1 if C in day else 0

    # 출력
    print(result)

if __name__ == "__main__":
    main()
