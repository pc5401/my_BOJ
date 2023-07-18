import heapq
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력과 전처리
    N = int(input())
    lst = [ list(map(int,input().split())) for i in range(N) ]

    lst.sort(key=lambda x : x[1]) # 강의 시작 시간으로 

    heap = [] # 힙 선언
    heapq.heappush(heap, lst[0][2]) # 첫 강의의 종료시간 삽입

    for i in range(1, N):
        # 가장 빨리 끝나는 강의 종료시간 vs 다음 강의 시작 시간
        if heap[0] > lst[i][1]: 
            heapq.heappush(heap, lst[i][2])
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, lst[i][2])

    print(len(heap))