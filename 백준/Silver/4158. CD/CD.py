import sys
import collections
input = sys.stdin.readline


if __name__ == '__main__':
    while 1:
        CD = collections.defaultdict(int)
        cnt = 0
        N, M = map(int,input().split())
        if N == 0 and M == 0:
            break

        for i in range(N):
            v = int(input())
            CD[v] = 1
        
        for i in range(M):
            v = int(input())
            if CD[v]:
                cnt += 1
                continue

        print(cnt)