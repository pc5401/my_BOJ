import sys
import heapq
input = sys.stdin.readline      


if __name__ == "__main__":
    # 입력값
    N = int(input())
    lst = [float(input()) for _ in range(N)]

    # 풀이
    heapq.heapify(lst)

    # 출력    
    for _ in range(7):
        v = heapq.heappop(lst)
        print(f'{v:.3f}')

