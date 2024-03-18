import sys
input = sys.stdin.readline


def main():
    A, B, N = map(int,input().split())
    A = A * (10**N)
    value = A // B
    print(value % 10)


if __name__ == "__main__":
    main()

