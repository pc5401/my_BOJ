import sys
import collections
input = sys.stdin.readline


def bfs(target: tuple, N: int, M: int) -> list:
    """ 최단거리 출력
    Args:
        target (tuple) : 목표지점 좌표
        N (int) : 행렬의 행 길이
        M (int) : 행렬의 열 길이
    
    Return:
        list : 전체 위치의 최단거리 출력
    """
    
    # bfs 세팅
    rtn = [[-1]*M for _ in range(N)]
    Queue = collections.deque()
    Queue.append(target)
    rtn[target[0]][target[1]] = 0

    while Queue:
        i, j = Queue.popleft()

        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < N and 0 <= nj < M and rtn[ni][nj] == -1:
                if arr[ni][nj]:
                    Queue.append((ni, nj))
                    rtn[ni][nj] = rtn[i][j] + 1
                else:
                    rtn[ni][nj] = 0

    # 도달 할 수 없는 부분을 따로 처리
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and rtn[i][j] != 0:
                rtn[i][j] = 0

    return rtn


def where_is(N: int, M: int) -> tuple:
    """ 타켓(2) 좌표 구하기(브루트 포스)
    Args: 
        N (int) : 행렬의 행 길이
        M (int) : 행렬의 열 길이

    Return:
        tuple : x, y 좌표
    """
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                return (i, j)

if __name__ == "__main__": # 최단거리 연습
    N, M = map(int, input().split())
    arr =[ list(map(int,input().split())) for _ in range(N)]
    
    target = where_is(N, M)
    res = bfs(target, N, M)
    # 결과 출력
    for r in res:
        print(*r)