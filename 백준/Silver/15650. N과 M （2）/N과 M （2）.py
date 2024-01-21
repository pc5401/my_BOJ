import sys
import itertools
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = itertools.combinations(range(1, N+1), M)
    for l in lst:
        print(*l)