import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    Q = list(map(int, input().split()))
    heapq.heapify(Q)

    for _ in range(N-1):
        arr = list(map(int, input().split()))
        while arr:
            a = arr.pop()
            if Q[0] < a:
                heapq.heappop(Q)
                heapq.heappush(Q,a)

    print(Q[0])