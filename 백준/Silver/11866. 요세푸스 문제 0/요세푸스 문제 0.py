import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int,input().split())
    Q = collections.deque(i for i in range(1, N+1))
    res = []

    while Q:
        for _ in range(K):
            Q.append(Q.popleft())
        res.append(Q.pop())

    print(str(res).replace('[','<').replace(']','>'))