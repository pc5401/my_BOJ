import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B = map(int, input().split())
    C = int(input())
    V = A + B
    if V >= C*2:
        print(V - C*2)
    else:
        print(V)