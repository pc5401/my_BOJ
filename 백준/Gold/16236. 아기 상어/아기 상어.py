import sys
import collections
input = sys.stdin.readline


def searchFood(shark: list) -> list: # 리런 [0],[1]: 좌표, [2]: 소요시간
    global N

    visit = [[0]*N for _ in range(N)]
    visit[shark[0]][shark[1]] = 1
    min_Time = -10
    food_lst = [] # 가장 가까운 먹이들
    Q = collections.deque()
    Q.append([shark[0], shark[1]])
    stop_Q = False
    while Q: # bfs
        v = Q.popleft()

        for d in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj]:
                if sea[ni][nj] > 0: # 일단 생선
                    if sea[ni][nj] > shark[2]: # 더 큼=벽
                        visit[ni][nj] = 100

                    elif sea[ni][nj] == shark[2]: # 같은 크기=길
                        visit[ni][nj] = visit[v[0]][v[1]] + 1
                        Q.append([ni, nj])

                    else: # 작은 크기 =음식
                        # 첫 음식
                        if min_Time < 0: 
                            min_Time = visit[v[0]][v[1]]
                            visit[ni][nj] = visit[v[0]][v[1]] + 1
                            Q.append([ni, nj])
                            food_lst.append([ni, nj, min_Time])
                        # 똑같은 거리
                        elif min_Time == visit[v[0]][v[1]]: 
                            visit[ni][nj] = visit[v[0]][v[1]] + 1
                            food_lst.append([ni, nj, min_Time])
                            Q.append([ni, nj])
                        # 없는 상황
                        elif min_Time > visit[v[0]][v[1]]: 
                            min_Time = visit[v[0]][v[1]]
                            food_lst = []
                            Q.append([ni, nj])
                            food_lst.append([ni, nj, min_Time])
                        # 거리가 멀어짐.
                        else:
                            stop_Q = True
                            break
                
                else: # 그냥 0
                    visit[ni][nj] = visit[v[0]][v[1]] + 1
                    Q.append([ni, nj])
        if stop_Q:
            break

    if not food_lst: # 빈 배열이면
        return []
    
    food_lst.sort(key=lambda x : (x[0], x[1]))

    return food_lst[0]

if __name__ == "__main__":
    N = int(input())
    Time = 0
    sea = [list(map(int,input().split())) for _ in range(N)]
    baby = [0,0,2,0] # 좌표(i,j), 레벨, 먹은 수
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                baby[0] = i
                baby[1] = j
                sea[i][j] = 0
    
    while True:
        food_fish = searchFood(baby) # 
        
        if food_fish: # 빈 list가 아니면
            # 좌표 변경
            baby[0] = food_fish[0]
            baby[1] = food_fish[1]
            baby[3] += 1 # 경험치 획득
            # 레벨 조정
            if baby[2] == baby[3]: 
                baby[2] += 1 # 레벨up
                baby[3] = 0 # 경험치 초기화
            # 시간 추가
            Time += food_fish[2]
            # 물고기 삭제
            sea[food_fish[0]][food_fish[1]] = 0
        else: # 먹이 없다.
            break

    print(Time)