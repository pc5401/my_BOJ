import sys
input = sys.stdin.readline

def throw_dice(dice_n: int,  idx: int, point: int, pos: list):
    global res

    if idx > 9: # 도착
        if point > res:
            res = point
            # print(f'dice_n": {dice_n}, idx: {idx}, point: {point}, pos: {pos}')
        return

    dice = dices[idx]

    if dice_n > 0 and not [0, dice] in pos: # 새로운 주사위
        pos.append([0, dice])
        throw_dice(dice_n - 1, idx+1, point + arr[0][dice], pos)
        pos.pop()

    for i in range(len(pos)): # 이미 던진 주사위 처리
        x, y = pos[i]
        
        if x == 0 and y % 5 == 0: # 파랑색 처리
            if y % 10 == 5 and dice > 3:
                a, b = 4, dice - 4
            elif y == 10 and dice > 2:
                a, b = 4, dice - 3
            else:
                a,b = (y * 2) // 10, dice-1
            
            if b >= len(arr[a]):
                b = len(arr[a]) - b
                a = 4


            if not [a, b] in pos:
                pos[i][0], pos[i][1] = a, b
                throw_dice(dice_n, idx+1, point + arr[a][b], pos)
                pos[i][0], pos[i][1] = x, y

        elif x == 0:
            a = 0
            b = y + dice
            if b > 20:
                dump_pos = pos[:]
                dump_pos.pop(i)
                throw_dice(dice_n, idx+1, point, dump_pos)
            elif b == 20:
                a = 4
                b = 3
                if not [a, b] in pos:
                    pos[i][0], pos[i][1] = a, b
                    throw_dice(dice_n, idx+1, point + arr[a][b], pos)
                    pos[i][0], pos[i][1] = x, y

            else:
                if not [a, b] in pos:
                    pos[i][0], pos[i][1] = a, b
                    throw_dice(dice_n, idx+1, point + arr[a][b], pos)
                    pos[i][0], pos[i][1] = x, y

        elif x == 4:
            a = 4
            b = y + dice
            if b > 3:
                dump_pos = pos[:]
                dump_pos.pop(i)
                throw_dice(dice_n, idx+1, point, dump_pos)
            else:
                if not [a, b] in pos:
                    pos[i][0], pos[i][1] = a, b
                    throw_dice(dice_n, idx+1, point + arr[a][b], pos)
                    pos[i][0], pos[i][1] = x, y

        else:
            b = y + dice
            if b >= len(arr[x]): 
                b = b - len(arr[x])
                if b > 3:
                    dump_pos = pos[:]
                    dump_pos.pop(i)
                    throw_dice(dice_n, idx+1, point, dump_pos)
                else:
                    a = 4
                    if not [a, b] in pos:
                        pos[i][0], pos[i][1] = a, b
                        throw_dice(dice_n, idx+1, point + arr[a][b], pos)
                        pos[i][0], pos[i][1] = x, y

            else: # 분기점까지 안 갈때,
                a = x
                if not [a, b] in pos:
                    pos[i][0], pos[i][1] = a, b
                    throw_dice(dice_n, idx+1, point + arr[a][b], pos)
                    pos[i][0], pos[i][1] = x, y


if __name__ == '__main__':
    dices = list(map(int,input().split()))
    arr = [
        [i*2 for i in range(20)],
        [13,16,19],
        [22,24],
        [28,27,26],
        [25,30,35,40],
        [0]
    ]
    res = 0
    throw_dice(4,0,0,[])
    print(res)