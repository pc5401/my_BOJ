import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A, B = 100, 100
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            B -= a
        elif a < b:
            A -= b
    print(A)
    print(B)
