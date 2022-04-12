# 시간 제한 문제(N:4~50과 M:1~10은 작음)
# 백트래킹 필요할듯
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

from pprint import pprint

input = sys.stdin.readline


def bfs(lst):
    global minV
    lab = deepcopy(arr)

    for i, j in lst:  # 시작이 0 이면 체크되니까.
        lab[i][j] = 1  # 1로 두고 마지막에 -1 해서 출력
    Q = deque()
    Q.extend(lst)

    while Q:

        v = Q.popleft()

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]

            if 0 <= ni < N and 0 <= nj < N and not lab[ni][nj]:
                lab[ni][nj] = lab[v[0]][v[1]] + 1
                Q.append([ni, nj])

                if lab[ni][nj] > minV:  # 가지치기
                    return

            elif 0 <= ni < N and 0 <= nj < N and lab[ni][nj] == '*':  # 엣지 케이스에 계속 걸림
                lab[ni][nj] = lab[v[0]][v[1]] + 1
                Q.append([ni, nj])


    for idx in virus:  # 바이러스 원상 복귀
        lab[idx[0]][idx[1]] = -1
    for w in wall:  # 벽처리
        lab[w[0]][w[1]] = -10

    value = -100
    for i in range(N): # 최대값 찾기 -> 가장 큰
        for j in range(N):
            if lab[i][j] > value:
                value = lab[i][j]
            if lab[i][j] == 0:
                return

    if value == -1:
        value = 1

    minV = min(minV, value) if value >= 0 else minV


N, M = map(int, input().split())
virus = []
arr = []
wall = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 2:
            virus.append([i,j])
            lst[j] = '*'
        elif lst[j] == 1:
            lst[j] = '-'
            wall.append([i, j])
    arr.append(lst)

virus_nCr = list(map(list, combinations(virus, M)))  # 경우의 수

minV = 1e9

for virus_lst in virus_nCr:  # 경우의 수를 일일이 넣었다.
    bfs(virus_lst)


print(-1 if minV == 1e9 else minV - 1)  # 못 채운 경우 '-1' 출력