import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    lst.sort()
    for i in lst:
        print(i)