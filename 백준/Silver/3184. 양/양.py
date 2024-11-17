import sys
import collections
input = sys.stdin.readline


def count_animal(r: int, c: int, R: int, C: int, arr: list[list[str]], visited:list[list[int]]) -> tuple[int, int]:
    w, s = 0, 0
    visited[r][c] = 1
    if arr[r][c] == 'v':
        w += 1
    elif arr[r][c] == 'o':
        s += 1
    
    Q = collections.deque()
    Q.append((r, c))

    while Q:
        i, j = Q.popleft()
        for d in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] == 'v':
                    w += 1
                elif arr[ni][nj] == 'o':
                    s += 1
                elif arr[ni][nj] == '#':
                    continue

                Q.append((ni, nj))
    
    return (w, s)


def solve(R: int, C: int, arr: list[str]):
    visited = [[0] * C for _ in range(R)] 
    wolf = 0
    sheep = 0
    for r in range(R):
        for c in range(C):
            if not visited[r][c] and arr[r][c] != '#':
                w, s = count_animal(r, c, R, C, arr, visited)
                if s > w:
                    sheep += s
                else:
                    wolf += w            
            else:
                visited[r][c] = 1
    
    return (sheep, wolf)
    

def main():
    # 입력값
    R, C = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(R)]
    # 결과 출력
    print(*solve(R,C,arr))

        
if __name__ == '__main__':
    main()