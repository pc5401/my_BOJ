import sys
input = sys.stdin.readline


if __name__ == "__main__":
    # 입력값, 데이터 세팅
    V, E = map(int, input().split())
    city_map = [[1e9]*V for _ in range(V)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        city_map[a-1][b-1] = min(c, city_map[a-1][b-1])
    # 플로이드 워셜
    for k in range(V):
        city_map[k][k] = 0
        for i in range(V):
            for j in range(V):
                city_map[i][j] = min(city_map[i][j], city_map[i][k]+city_map[k][j])
    
    res = 1e9
    for i in range(V):
        for j in range(V):
            if i == j:
                continue
            res = min(res, city_map[i][j] + city_map[j][i])
    print(res if res < 1e9 else -1)
