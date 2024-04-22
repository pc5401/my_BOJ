import sys
input = sys.stdin.readline


def is_bingo(checked) -> bool:
    cnt = 0

    if all([checked[i][i] for i in range(5)]):
        cnt += 1
    
    if all([checked[i][4 - i] for i in range(5)]):
        cnt += 1

    for i in range(5):
        if all(checked[i]):
            cnt += 1
        
        if all([checked[j][i] for j in range(5)]):
            cnt += 1

    if cnt < 3:
        return False
    else:
        return True


def check(num: int, board: list[list[int]]) -> tuple[int, int]:

    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return (i, j)


def solve(board: list[list[int]], bingo_order: list[int]) -> int:
    checked = [[0] * 5 for _ in range(5)]

    for cnt, num in enumerate(bingo_order, start=1):
        x, y = check(num, board)
        checked[x][y] = 1
        if is_bingo(checked):
            return cnt
    
    return -1


def main():
    # 입력값
    board: list[list[int]] = [list(map(int, input().split())) for _ in range(5)]
    bingo_order: list[int] = [num for _ in range(5) for num in map(int, input().split())]
    # 풀이
    result: int = solve(board, bingo_order)
    # 출력
    print(result)


if __name__ == "__main__":
    main()