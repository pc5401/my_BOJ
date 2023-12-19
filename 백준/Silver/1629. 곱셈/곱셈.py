import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    def func(a, b, c):
        if b == 0:
            return 1
        elif b % 2 == 0:
            y = func(a, b // 2, c)
            return (y * y) % c
        else:
            return (a * func(a, b-1, c)) % c

    print(func(A, B, C))