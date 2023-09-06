import sys
import collections
input = sys.stdin.readline

def order(blue: int, red: int, dir: int) -> str: # 조건 분기
    if dir == 0: # 앞으로 기울임
        if blue[0] < red[0]:
            return 'blue'
        else:
            return 'red'
        
    elif dir == 1: # 안쪽으로 기울임
        if blue[0] < red[0]:
            return 'red'
        else:
            return 'blue'
        
    elif dir == 2: # 왼쪽 올리고, 오른쪽 내림 ->
        if blue[1] < red[1]:
            return 'red'
        else:
            return 'blue'
        
    elif dir == 3: # 오른쪽 올리고, 왼쪽 내림 <-
        if blue[1] < red[1]:
            return 'blue'
        else:
            return 'red'


def fist_moving(ball:list, dir: int):
    i, j = ball
    while 1:
        ni = i + delta[dir][0]
        nj = j + delta[dir][1]
        if board[ni][nj] == 'O':
            return [11, 11]
        
        elif board[ni][nj] == '#': # stop
            return [i, j]
        
        i = ni
        j = nj

def second_moving(ball:list, dir: int, first_ball:list):
    i, j = ball
    while 1:
        ni = i + delta[dir][0]
        nj = j + delta[dir][1]
        if board[ni][nj] == 'O':
            return [11, 11]
        
        elif ni == first_ball[0] and nj == first_ball[1]:  # stop
            return [i, j]
        
        elif board[ni][nj] == '#': # stop
            return [i, j]
        i = ni
        j = nj

def move(blue: list, red: list, dir: int, first_move: str) -> tuple:
    # 이동 방향 + 어떤 볼 부터 움직일찌.
    if first_move == 'blue':
        new_blue = fist_moving(blue, dir)
        new_red = second_moving(red, dir, new_blue)
        
        if new_blue[0] == 11: # 홀에 빠짐
            return [-1, -1], [-1, -1]
        
        elif new_red[0] == 11: # 홀에 빠짐
            return [11, 11], [11, 11]
    
    else:
        new_red = fist_moving(red, dir)
        new_blue = second_moving(blue, dir, new_red)
        
        if new_blue[0] == 11: # 홀에 빠짐
            return [-1, -1], [-1, -1]
        
        elif new_red[0] == 11: # 홀에 빠짐
            return [11, 11], [11, 11]
        
    if new_blue[0] == blue[0] and new_blue[1] == blue[1] and new_red[0] == red[0] and new_red[1] == red[1]:
        return  [-1, -1], [-1, -1]
        
    return new_blue ,new_red

if __name__ == '__main__':
    # 입력값 초기값 세팅
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        lst = list(input())[:-1]
        for j in range(M):
            if lst[j] == 'B':
                B = [i,j]
            elif lst[j] == 'R':
                R = [i,j]
        board.append(lst)
    
    delta = [[-1,0],[1,0],[0,1],[0,-1]] # 상하좌우
    Q = collections.deque()
    Q.append([1, B, R])

    while Q:

        cnt, b, r = Q.popleft()
        if cnt >= 11:
            break

        for d in range(4):
            new_b, new_r = move(b,r,d, order(b,r,d))
            if new_b[0] == 11:

                print(cnt)
                exit()

            elif new_b[0] == -1:
                continue

            Q.append([cnt+1, new_b, new_r])

    print(-1)