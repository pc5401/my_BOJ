import sys
input = sys.stdin.readline

def winner(table: list) -> tuple:
    X_win = 0
    O_win = 0

    for i in range(3):
        if table[i][0] == table[i][1] and table[i][0] == table[i][2]:
            if table[i][0] == 'X':
                X_win += 1
            elif table[i][0] == 'O':
                O_win += 1

    for j in range(3):
            if table[0][j] == table[1][j] and table[0][j] == table[2][j]:
                if table[0][j] == 'X':
                    X_win += 1
                elif table[0][j] == 'O':
                    O_win += 1

    if table[0][0] == table[1][1] and table[0][0] == table[2][2]:
        if table[0][0] == 'X':
            X_win += 1
        elif table[0][0] == 'O':
            O_win += 1

    if table[0][2] == table[1][1] and table[0][2] == table[2][0]:
        if table[0][2] == 'X':
            X_win += 1
        elif table[0][2] == 'O':
            O_win += 1

    return X_win, O_win

def solve(table: list):
    X_cnt = data.count('X')
    O_cnt = data.count('O')
    
    if O_cnt > X_cnt or (X_cnt - O_cnt) > 1: # 돌의 수가 맞지 않는 경우
        return 'invalid'
    
    if O_cnt < 3 and X_cnt < 3:
        return 'invalid'
    
    X_win_cnt, O_win_cnt = winner(table)

    if O_win_cnt == 0 and X_win_cnt == 0: # 승부가 나지 않음
        if X_cnt == 5 and O_cnt == 4: # 돌 다 소모 게임 종료
            return 'valid'
        
        return 'invalid' # 지들 맘대로 종료함
    
    if O_win_cnt > 1 and X_win_cnt > 1: # 서로 한 번 이상 이김?
        return 'invalid'
    
    if O_win_cnt > 0 and (X_cnt > O_cnt): # O 이 이겼는데 X가 돌 둠.
        return 'invalid'
    
    if X_win_cnt > 0 and (X_cnt == O_cnt): # X 이 이겼는데 O가 돌 둠.
        return 'invalid'
    

    return 'valid'


if __name__ == '__main__':
    # 초기값 
    res = []
    while True:
        data = list(input().split()[0])
        if data[0]=='e':
            break
        table = [[data[i], data[i+1], data[i+2]] for i in range(0, 7, 3)]
        print(solve(table))
