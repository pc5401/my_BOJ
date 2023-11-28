import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(max(B-A, C-B)-1)

