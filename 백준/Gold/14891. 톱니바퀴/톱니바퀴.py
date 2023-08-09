import sys
input = sys.stdin.readline


def turn(lst: list, dir: int):
    if dir > 0:
        copy = [lst[7]]
        copy.extend(lst[:7])
    
    else:
        copy = lst[1:]
        copy.append(lst[0])
    
    return copy

def movement(target: int, dir: int):
    visit = [0] * 4
    visit[target] = 1
    
    Q = []
    Q.append([target, dir])

    while Q:
        n, d = Q.pop() # n 현재위치, b 이전 톱니바퀴, d 방향

        if n + 1 < 4 and not visit[n+1] and tob[n][2] != tob[n+1][6]:
            visit[n+1] = 1
            Q.append([n+1, d * -1])

        if n - 1 >= 0 and not visit[n-1] and tob[n][6] != tob[n-1][2]:
            visit[n-1] = 1
            Q.append([n-1, d * -1])
        
        tob[n] = turn(tob[n], d)


if __name__ == '__main__':
    tob=[ list(map(int,input().strip())) for _ in range(4) ] # 0 = N, 1 = S 
    K = int(input())

    for _ in range(K):
        target, dir = map(int,input().split())
        movement(target-1, dir)

    res = 0

    if tob[0][0]:
        res += 1
    if tob[1][0]:
        res += 2
    if tob[2][0]:
        res += 4
    if tob[3][0]:
        res += 8
    
    print(res)
