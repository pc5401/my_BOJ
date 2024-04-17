import sys
input = sys.stdin.readline


def solve(n: int, m: int, tray: list[str]) -> int:
    rtn = 0
    visited = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            if tray[i][j] == '>' and j+2 < m:
                if tray[i][j+1] == 'o' and tray[i][j+2] == '<':
                    rtn += 1
                    visited[i][j], visited[i][j+1], visited[i][j+2] = 1, 1, 1
                else:
                    visited[i][j] = 1
            
            elif tray[i][j] == 'v' and i+2 < n:
                if tray[i+1][j] == 'o' and tray[i+2][j] == '^':
                    rtn += 1
                    visited[i][j], visited[i+1][j] , visited[i+2][j] = 1, 1, 1
                else:
                    visited[i][j] = 1
            else:
                visited[i][j] = 1
    return rtn



def main():
    # 입력값
    result = []
    T: int = int(input())
    for _ in range(T):
        empty = input()
        N, M = map(int, input().split())
        tray = [input().rstrip() for _ in range(N)]
        result.append(solve(N, M, tray))

    for res in result:
        print(res)

if __name__ == "__main__":
    main()