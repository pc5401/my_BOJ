import sys
input = sys.stdin.readline

def move_clouds(lst:list, cloud:list) -> list:
    d, s = lst[0], lst[1]

    for idx, c in enumerate(cloud):
        i, j = c[0], c[1]
    
        ni = i + (delta[d][0] * s)
        if 0 > ni or ni >= N:
            v = ni % N
            ni = v if v >= 0 else N + v
        
        nj = j + (delta[d][1] * s)
        if 0 > nj or nj >= N:
            v = nj % N
            nj = v if v >= 0 else N + v
        cloud[idx][0] = ni
        cloud[idx][1] = nj
        arr[ni][nj] += 1
    
    return cloud

def water_bug(bf_cloud:list):
    new_cloud = []
    rm_cloud = set(map(tuple, bf_cloud))
    degac = [[-1,-1], [-1,1], [1,-1],[1,1]]
    
    for c in rm_cloud:
        for d in degac:
            ni = c[0] + d[0]
            nj = c[1] + d[1]
            if ni >= 0 and N > ni and nj >= 0 and N > nj and arr[ni][nj]:
                arr[c[0]][c[1]] += 1

    for i in range(N):
        for j in range(N):
            if (i,j) in rm_cloud:
                continue

            if arr[i][j] > 1: 
                arr[i][j] -= 2
                new_cloud.append([i,j])

    return new_cloud

if __name__ == "__main__":
    # input 값
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    moves = [list(map(int,input().split())) for _ in range(M)]
    # 사용할 데이터 값
    clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2,1]]
    delta = [[0,0], [0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]
    for i in moves:
        clouds = water_bug(move_clouds(i,clouds))

    res = 0
    for n in range(N):
        res += sum(arr[n])

    print(res)
