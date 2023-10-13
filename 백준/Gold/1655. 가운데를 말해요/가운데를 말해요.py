import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    result, left, right = [], [], []
    le, ri = 0, 0
    for _ in range(N):
        n = int(input())
        if not left or n <= -left[0]:
            heapq.heappush(left, -n)
        else:
            heapq.heappush(right, n)
            
        # 수 맞추기
        while len(left) < len(right):
            v = heapq.heappop(right)
            heapq.heappush(left, -v)
            
        while len(left) > len(right) + 1:
            v = -heapq.heappop(left)
            heapq.heappush(right, v)

        result.append(-left[0])
    for r in result:
        print(r)
