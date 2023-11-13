import sys
import itertools
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    arr = list(set(itertools.permutations(lst, M)))
    result = sorted(arr)
    for res in result:
        print(*res)