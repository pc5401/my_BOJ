import sys
input = sys.stdin.readline

def block_cnt(lst: list) -> int:
    res = 0
    for i in lst:
        res += sum(i)
    return res


def translate_to_blue(t: int, x: int, y: int) -> tuple:
    # t -> return_t
    ry = 3 - x
    rx = y
    if t == 1: 
        rt = 1
    elif t == 2: 
        rt = 3
        rx += 1
    elif t == 3:
        ry -= 1
        rt = 2
    
    return (rt, rx, ry)

# 올린 점수 만큼 블록 지우고 채우기
def score_up(line: list, lst: list) -> list:
    n = len(line)
    new_lst = [[0]*4 for _ in range(n)]
    
    for i in range(6):
        if i in line:
            continue
        new_lst.append(lst[i])

    return new_lst

# 하늘색 처리
def sky_done(n: int, lst: list) -> list:
    new_lst = [[0]*4 for _ in range(n)]

    for i in range(n):
        lst.pop()

    new_lst.extend(lst)

    return new_lst



def stack_block(lst: list, t: int, x: int, y: int) -> list:
    global score

    # 블록 쌓기
    if t == 1:
        for i in range(7):
            if i == 6 or lst[i][y]:
                lst[i-1][y] = 1
                break
    
    elif t == 2:
        for i in range(7):
            if i==6 or lst[i][y] or lst[i][y+1]:
                lst[i-1][y], lst[i-1][y+1] = 1, 1
                break
    
    elif t == 3:
        for i in range(7):
            if i == 6 or lst[i][y]:
                lst[i-1][y], lst[i-2][y] = 1, 1
                break

    # 한 줄 만들었는지 확인
    line = []
    for i in range(5, 1, -1):
        if sum(lst[i]) == 4:
            line.append(i)
            score += 1
    if line:
        lst = score_up(line, lst)

    # 하늘색 구역 확인
    sky = 0
    for i in range(2):
        if sum(lst[i]) > 0:
            sky += 1
    if sky:
        lst = sky_done(sky, lst)

    return lst

if __name__ == '__main__':
    T = int(input()) # 입력값 횟수

    # 데이터 전처리
    block_momel = {1:[(0,0)], 2:[(0,0),(0,1)], 3:[(0,0),(1,0)]}
    green = [[0] * 4 for _ in range(6)]
    blue = [[0] * 4 for _ in range(6)]
    score = 0
    # 입력값 및 계산
    for tc in range(T):
        gt, gx, gy = map(int,input().split())
        bt, bx, by = translate_to_blue(gt,gx,gy)
        green = stack_block(green, gt, gx, gy)
        blue = stack_block(blue, bt, bx, by)

    # 출력값
    res = block_cnt(green) + block_cnt(blue)
    print(score)
    print(res)