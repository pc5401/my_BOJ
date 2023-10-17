import sys
input = sys.stdin.readline

def blizzard(N: int, di: int, si: int, Arr: list) -> list:
    # 블리자드 마법 후 1 차원 배열
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    d = dir[di-1]
    x, y =  N//2,  N//2
    for s in range(1, si+1):
        Arr[x + d[0]*s][y + d[1]*s] = 0

    rtn = []
    d = 0
    delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for n in range(1, N):

        for i in range(n):
            x += delta[d][0]
            y += delta[d][1]
            if Arr[x][y] > 0:
                rtn.append(Arr[x][y])
        d = (d+1)%4

        for i in range(n):
            x += delta[d][0]
            y += delta[d][1]
            if Arr[x][y] > 0:
                rtn.append(Arr[x][y])
        d = (d+1)%4
    
    for j in range(y-1, -1, -1):
        if Arr[0][j] > 0:
                rtn.append(Arr[0][j])
    return rtn

def bomb(lst: list) -> list:
    global res
    # 구슬 폭발 및 정렬

    while True:
        idxs = []
        if not lst:
            return []
        cnt, num = 1, lst[0]
        for i in range(1, len(lst)):
            if lst[i] != num and cnt < 4:
                num = lst[i]
                cnt = 1
            elif lst[i] != num:
                for c in range(cnt):
                    idxs.append(i-cnt+c)
                num = lst[i]
                cnt = 1
            else:
                cnt += 1
            
        if cnt > 3:
            for j in range(cnt):
                idxs.append(i-cnt+j)

        if not idxs:
            break
        while idxs:
            res += lst.pop(idxs.pop())
        
    return lst


def count_marble(lst: list) -> list:
    rtn = []
    if not lst:
        return []
    cnt, num = 1, lst[0]
    for i in range(1, len(lst)):
        if num == lst[i]:
            cnt += 1
        else:
            rtn.append(cnt)
            rtn.append(num)
            cnt = 1
            num = lst[i]
    rtn.append(cnt)
    rtn.append(num)

    return rtn


def make_load(N) -> list:
    rtn = []
    d, idx = 0,0
    x, y =  N//2,  N//2
    delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for n in range(1, N):
        for i in range(n):
            x += delta[d][0]
            y += delta[d][1]
            rtn.append((x,y))
        d = (d+1)%4

        for i in range(n):
            x += delta[d][0]
            y += delta[d][1]
            rtn.append((x,y))
        d = (d+1)%4
    
    for j in range(y-1, -1, -1):
        rtn.append((0,j))
    return rtn


def new_Arr(N: int, lst: list, load: list) -> list:
    arr = [[0]*N for _ in range(N)]
    for i, v in enumerate(lst):
        try:
            x, y = load[i]
            arr[x][y] = v
        except:
            break

    return arr


def solve(N: int, M: int, Arr: list) -> int:
    load = make_load(N)
    for di, si in Masics:
        lst = count_marble(bomb(blizzard(N, di, si, Arr)))
        Arr = new_Arr(N, lst, load)

    # for a in Arr:
    #     print(a)
    
    return res


if __name__ == "__main__":
    # 입력 & 전처리
    res = 0
    N, M = map(int, input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    Masics = [tuple(map(int, input().split())) for _ in range(M)]
    solve(N, M, Arr)
    print(res)
