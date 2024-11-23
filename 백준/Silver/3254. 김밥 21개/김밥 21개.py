import sys

def solve(throws):
    grid = [['0' for _ in range(7)] for _ in range(6)]
    winner = None
    M = None
    S_count = 0
    J_count = 0

    def check_win(r, c, player):
        directions = [(0,1),(1,0),(1,1),(1,-1)]
        for dr, dc in directions:
            count = 1
            nr, nc = r + dr, c + dc
            while 0 <= nr <6 and 0 <= nc <7 and grid[nr][nc] == player:
                count +=1
                nr += dr
                nc += dc
            nr, nc = r - dr, c - dc
            while 0 <= nr <6 and 0 <= nc <7 and grid[nr][nc] == player:
                count +=1
                nr -= dr
                nc -= dc
            if count >=4:
                return True
        return False

    for throw in throws:
        S_move, J_move = throw

        # 상근이의 던짐 처리
        S_count +=1
        col_s = S_move -1
        row_s = -1
        for r in range(5, -1, -1):
            if grid[r][col_s] == '0':
                grid[r][col_s] = 'S'
                row_s = r
                break
        # 김밥을 성공적으로 놓았는지 확인
        if row_s != -1 and not winner:
            if check_win(row_s, col_s, 'S'):
                winner = 'sk'
                M = S_count

        # 정인이의 던짐 처리
        J_count +=1
        col_j = J_move -1
        row_j = -1
        for r in range(5, -1, -1):
            if grid[r][col_j] == '0':
                grid[r][col_j] = 'J'
                row_j = r
                break
        # 김밥을 성공적으로 놓았는지 확인
        if row_j != -1 and not winner:
            if check_win(row_j, col_j, 'J'):
                winner = 'ji'
                M = J_count

    if winner:
        return f"{winner} {M}"
    else:
        return "ss"

def main():
    input = sys.stdin.read().splitlines()
    # 입력이 21줄이므로 21개의 튜플을 생성
    throws = []
    for line in input:
        if line.strip() == '':
            continue  # 빈 줄은 무시
        parts = line.strip().split()
        if len(parts) != 2:
            continue  # 두 개의 숫자가 아닌 경우 무시
        S, J = map(int, parts)
        throws.append((S, J))
    # 실제 게임에서는 21번 던짐마다 상근이와 정인이가 각각 던짐
    # 따라서 총 42번의 던짐을 순차적으로 처리
    all_throws = []
    for throw in throws:
        all_throws.append(throw)  # (S, J)

    # 이제 상근이와 정인이가 번갈아 던짐을 순서대로 처리
    # 첫 번째 던짐은 상근이, 두 번째는 정인이, 세 번째은 상근이, ...
    sequential_throws = []
    for throw in all_throws:
        sequential_throws.append(('S', throw[0]))  # 상근이의 던짐
        sequential_throws.append(('J', throw[1]))  # 정인이의 던짐

    # solve 함수는 (player, column) 형태의 리스트를 받도록 수정
    def solve_updated(throws_seq):
        grid = [['0' for _ in range(7)] for _ in range(6)]
        winner = None
        M = None
        S_count = 0
        J_count = 0

        def check_win(r, c, player):
            directions = [(0,1),(1,0),(1,1),(1,-1)]
            for dr, dc in directions:
                count = 1
                nr, nc = r + dr, c + dc
                while 0 <= nr <6 and 0 <= nc <7 and grid[nr][nc] == player:
                    count +=1
                    nr += dr
                    nc += dc
                nr, nc = r - dr, c - dc
                while 0 <= nr <6 and 0 <= nc <7 and grid[nr][nc] == player:
                    count +=1
                    nr -= dr
                    nc -= dc
                if count >=4:
                    return True
            return False

        for throw in throws_seq:
            player, col = throw
            if player == 'S':
                S_count +=1
                current_count = S_count
                symbol = 'S'
            else:
                J_count +=1
                current_count = J_count
                symbol = 'J'
            col_idx = col -1
            row = -1
            for r in range(5, -1, -1):
                if grid[r][col_idx] == '0':
                    grid[r][col_idx] = symbol
                    row = r
                    break
            if row == -1:
                continue  # 열이 꽉 찬 경우, 문제에서 발생하지 않음
            if not winner:
                if check_win(row, col_idx, symbol):
                    winner = 'sk' if player == 'S' else 'ji'
                    M = current_count
        if winner:
            return f"{winner} {M}"
        else:
            return "ss"

    result = solve_updated(sequential_throws)
    print(result)

if __name__ == "__main__":
    main()
