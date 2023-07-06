import sys
import collections
input = sys.stdin.readline


if __name__ == '__main__':
    while 1:
        N, M = map(int,input().split())
        if N == 0 and M == 0:
            break

        data = set()
        for i in range(N):
            data.add(int(input()))

        for i in range(M):
            data.add(int(input()))

        print((N+M)-len(data))