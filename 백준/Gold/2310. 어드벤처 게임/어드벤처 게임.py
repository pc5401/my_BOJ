import sys
import collections
input = sys.stdin.readline


def bfs(now: int, n:int, miro: list) -> str:
    miro[0][0] = 0
    Q = collections.deque()
    Q.append(now)
    while Q:
        now = Q.popleft()
        money, room = miro[now][0], miro[now]

        if room[1] == 'L':
            money = max(money, room[2])
        elif room[1] == 'T':
            money -= room[2]
            if money < 0:
                continue
        
        if now == (n-1):
            return 1
        
        for i in room[3:-1]:
            next = (i-1)
            if miro[next][0] < money or miro[next][0] == -1:
                miro[next][0] = money
                Q.append(next)
    return 0

if __name__ == "__main__":
    while 1:
        N = int(input())
        if N:
            miro = [[-1]+ list(map(lambda x : int(x) if x.isdigit() else x, input().split())) for _ in range(N) ]
            
            print('Yes' if bfs(0, N, miro) else 'No')
        else:
            break