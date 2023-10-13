import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    res = []
    heap = []
    for _ in range(N):
        n = int(input())
        if n:
            heapq.heappush(heap, -n)
        else:
            if heap:
                res.append(-heapq.heappop(heap))
            else:
                res.append(0)

    for r in res:
        print(r)
