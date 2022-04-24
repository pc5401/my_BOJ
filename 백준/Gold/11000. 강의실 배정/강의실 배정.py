# 구글링해서 겨우 품ㅠㅠ

import sys
import heapq
input = sys.stdin.readline

N = int(input())
times = []
room = []
for n in range(N):  # 입력값 리스트에 넣어줌
    s, t = map(int, input().split())
    times.append([s, t])

times.sort() # 자동으로 정렬
heapq.heappush(room, times[0][1])  # 가장 먼저. 끝시간

for i in range(1, N):  # 끝나는 시간 넣어줌
    if room[0] > times[i][0]: # 시간 비교
        heapq.heappush(room, times[i][1])  # 안 빼고 넣고

    else:
        heapq.heappop(room)  # 빼고
        heapq.heappush(room, times[i][1]) # 넣고

print(len(room))
