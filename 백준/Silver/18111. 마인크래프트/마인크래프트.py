import sys
input = sys.stdin.readline


def h_time(target: int, b: int)-> int:
    global N, M
    time = 0

    for i in range(N):
        for j in range(M):
            dist = target - land[i][j]
            if dist > 0: # 블록 쌓기
                time += dist
            elif dist < 0: # 블록 파기
                time += dist * (-2)
            
            b -= dist
    
    if b < 0:
        return float('INF')
    return time


if __name__ == "__main__":
    N, M, B = map(int,input().split())
    land = [list(map(int,input().split())) for _ in range(N)]
    res_h, res_time = 0, float('INF')

    for h in range(257):
        time = h_time(h, B)
        if time <= res_time:
            res_time = time
            res_h = h
        else:
            break
    
    print(res_time, res_h)
