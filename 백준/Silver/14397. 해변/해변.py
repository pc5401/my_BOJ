import sys
input = sys.stdin.readline


def world_count(i: int, j: int, N: int, M: int, worlds:list[list[str]]):
    cnt = 0
    if i % 2: # 홀수
        delta = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]
    else:
        delta =  [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]

    for x, y in delta:
        ni = i + x
        nj = j + y
        if 0 <= ni < N and 0 <= nj < M and worlds[ni][nj] == '.':
            cnt += 1

    return cnt


def solve(N: int, M: int, worlds:list[list[str]]) -> int:
    rtn = 0
    
    for i in range(N):
        for j in range(M):
            if worlds[i][j] == '.':
                continue
            rtn += world_count(i, j, N, M, worlds)

    return rtn

def main():
    # 입력값
    N, M = map(int, input().split())
    worlds = [list(input().rstrip()) for _ in range(N)]
    
    # 풀이
    result = solve(N, M, worlds)

    # 출력
    print(result)


if __name__ == "__main__":
    main()

