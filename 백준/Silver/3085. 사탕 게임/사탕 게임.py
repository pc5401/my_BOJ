import sys
input = sys.stdin.readline

def max_search(board, N):
    best = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                if cnt > best:
                    best = cnt
                cnt = 1
        if cnt > best:
            best = cnt
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                if cnt > best:
                    best = cnt
                cnt = 1
        if cnt > best:
            best = cnt
    return best

def solve(N, board):
    A = [list(row) for row in board]
    ans = 1
    for i in range(N):
        for j in range(N):
            if j + 1 < N and A[i][j] != A[i][j+1]:
                A[i][j], A[i][j+1] = A[i][j+1], A[i][j]
                v = max_search(A, N)
                if v > ans:
                    ans = v
                A[i][j], A[i][j+1] = A[i][j+1], A[i][j]
            if i + 1 < N and A[i][j] != A[i+1][j]:
                A[i][j], A[i+1][j] = A[i+1][j], A[i][j]
                v = max_search(A, N)
                if v > ans:
                    ans = v
                A[i][j], A[i+1][j] = A[i+1][j], A[i][j]
    return ans

def main():
    # 입력
    N = int(input().strip())
    board = [input().strip() for _ in range(N)]

    # 풀이
    result = solve(N, board)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
