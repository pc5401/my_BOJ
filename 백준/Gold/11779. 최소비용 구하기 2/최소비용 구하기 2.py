import sys
import heapq
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력값 처리
    n = int(input())
    m = int(input())
    bus_info = collections.defaultdict(list)
    for _ in range(m):
        a, b, cost = map(int,input().split())
        bus_info[a].append((b, cost))
        # bus_info[b].append((a, cost))
    start, end = map(int, input().split())

    # 데이터 전처리
    distance = [float('INF')]*(n+1)
    bus_path = [0] * (n+1)
    Queue = [(start, 0)]
    distance[start] = 0

    while Queue:
        now, dist = heapq.heappop(Queue)

        if distance[now] < dist:
            continue

        for next, cost in bus_info[now]:
            if distance[next] > dist + cost:
                distance[next] = dist + cost
                bus_path[next] = now
                heapq.heappush(Queue,(next, dist + cost))
    
    # 경로 탐색
    res = []
    bus_num = end
    while bus_num:
        res.append(bus_num)
        if bus_num == start:
            break
        bus_num = bus_path[bus_num]

    # 결과 출력
    print(distance[end])
    print(len(res))
    print(*res[::-1])
