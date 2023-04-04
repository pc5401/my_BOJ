# chatGPT가 알려준 시간 개선안, python으로 통과할 수 있는지 테스트

from collections import defaultdict

R, C, M = map(int, input().split())
sharks = defaultdict(list)  # 상어 정보를 저장할 딕셔너리
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = [r-1, c-1, s, d-1, z]  # 좌표는 0부터 시작

ans = 0  # 총 잡은 상어 크기의 합
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 상, 하, 우, 좌 방향 벡터
for j in range(C):
    # 1. 낚시
    min_dist = R  # 가장 가까운 상어까지의 거리
    min_shark = None  # 가장 가까운 상어의 번호
    for i in range(R):
        if sharks[(i, j)]:
            if i < min_dist:
                min_dist = i
                min_shark = (i, j)
            break
    if min_shark:
        ans += sharks[min_shark][4]
        sharks[min_shark] = None

    # 2. 상어 이동
    new_sharks = defaultdict(list)
    for (r, c), info in sharks.items():
        if not info:  # 이미 낚시당한 상어면 continue
            continue
        s, d, z = info[2:]
        nr, nc = r + s * delta[d][0], c + s * delta[d][1]
        while not (0 <= nr < R and 0 <= nc < C):  # 벽에 부딪힐 때마다 방향을 전환하면서 이동
            if nr < 0:
                nr = -nr
                d = 1
            elif nr >= R:
                nr = 2 * (R-1) - nr
                d = 0
            elif nc < 0:
                nc = -nc
                d = 2
            elif nc >= C:
                nc = 2 * (C-1) - nc
                d = 3
        if new_sharks[(nr, nc)] and new_sharks[(nr, nc)][4] > z:  # 이미 다른 상어가 있을 경우 크기 비교 후 작은 상어는 제거
            continue
        new_sharks[(nr, nc)] = [nr, nc, s, d, z]
    sharks = new_sharks

print(ans)