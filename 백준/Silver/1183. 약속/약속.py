import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A, B, C = [], [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(a-b)
    
    C.sort()
    if N % 2:
        print(1)
    else:
        x, y = (N // 2) - 1, N // 2
        print(abs(C[x]-C[y]) + 1)


if __name__ == "__main__":
    main()
