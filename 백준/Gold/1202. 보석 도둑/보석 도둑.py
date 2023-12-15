import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    gems = [tuple(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]
    
    # 정렬
    gems.sort(key=lambda x: -x[0])
    bags.sort()
    
    res = 0
    Q = []
    for bag in bags:
        while gems:
            gem = gems.pop()
            if gem[0] > bag:
                gems.append(gem)
                break
            heapq.heappush(Q, (-gem[1], gem[0]))
        
        while Q:
            V, M = heapq.heappop(Q)
            if M <= bag:
                res -= V
                break
    print(res)