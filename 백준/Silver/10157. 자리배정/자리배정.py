import sys
input = sys.stdin.readline


def solve(c: int, r: int, k: int) -> int:
    visited = [[0]*c for _ in range(r)]
    visited[0][0] = 1
    delta = [[0,1],[1,0],[0,-1],[-1,0]]
    dir = 0

    if k > c*r:
        return [0]

    i, j = 0, 0

    while visited[i][j] < c*r:
        if visited[i][j] == k:
            return [i+1, j+1]
        
        ni = i + delta[dir][0]
        nj = j + delta[dir][1]
        
        if 0 <= ni < r and 0 <= nj < c and not visited[ni][nj]:
            visited[ni][nj] = visited[i][j] + 1
            i, j = ni, nj
        else:
            dir = (dir+1) % 4

    return [0] if visited[i][j] != k else [i+1, j+1]


def main():
    # 입력값
    c, r = map(int, input().split())
    k = int(input())
    # 풀이
    result: list[int] = solve(r,c, k)
    # 출력
    print(*result)


if __name__ == "__main__":
    main()