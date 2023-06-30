import heapq
import sys
input = sys.stdin.readline

def dijkstra(N: int, K: int):
    # 모든 위치를 도달하는데 필요한 시간을 무한대로 초기화
    INF = int(1e9)
    time = [INF] * 100001
    time[N] = 0  # 시작 위치의 시간은 0
    
    # 우선 순위 큐에 시작 위치와 시간을 추가
    q = [(0, N)]  # (시간, 위치)
    
    while q:
        cur_time, cur_pos = heapq.heappop(q)

        # 현재 위치가 동생이 있는 위치인 경우, 시간을 반환
        if cur_pos == K:
            return cur_time
        
        # 현재 위치에서 이동 가능한 모든 위치를 확인
        for next_pos in [cur_pos * 2, cur_pos + 1, cur_pos - 1]:
            # 다음 위치가 범위 내에 있는 경우
            if 0 <= next_pos <= 100000:
                # 다음 위치로 이동하는데 필요한 시간
                # 순간이동인 경우 시간이 증가하지 않음
                next_time = cur_time if next_pos == cur_pos * 2 else cur_time + 1
                
                # 다음 위치로의 이동 시간이 이전에 구한 시간보다 작은 경우
                if next_time < time[next_pos]:
                    time[next_pos] = next_time  # 시간을 갱신
                    heapq.heappush(q, (next_time, next_pos))  # 우선 순위 큐에 추가

if __name__ == '__main__':
    n, k = map(int,input().split())
    print(dijkstra(n, k))
# 올랜만에 다익스트라 복습했다. ㅠ