import sys
input = sys.stdin.readline

def solve(graph: list[str]) -> int:
    board_init = [[1 if ch == 'O' else 0 for ch in row] for row in graph]
    INF = float('inf')
    ans = INF

    # 스위치 누르기
    def press(board, i, j):
        for di, dj in [(0,0), (1,0), (-1,0), (0,1), (0,-1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 10 and 0 <= nj < 10:
                board[ni][nj] = 1 - board[ni][nj]
    

    for mask in range(1 << 10):
        board = [row[:] for row in board_init]
        cnt = 0
        
        for j in range(10):
            if mask & (1 << j):
                cnt += 1
                press(board, 0, j)
        
        
        for i in range(9):
            for j in range(10):
                if board[i][j] == 1:
                    cnt += 1
                    press(board, i+1, j)
        
        if all(cell == 0 for cell in board[9]):
            ans = min(ans, cnt)
    
    return ans if ans != INF else -1

def main():
    # 입력
    graph = [list(input().rstrip()) for _ in range(10)]

    # 풀이
    result = solve(graph)

    # 출력
    print(result)

if __name__ == "__main__":
    main()