import sys
input = sys.stdin.readline


def main():
    # 입력값
    N = int(input())

    if N == 1:
        res = 0
    elif N == 2:
        res = 2
    else:
        res = 2*(3**(N-2)) % 1_000_000_009

    print(res)

if __name__ == "__main__":
    main()
