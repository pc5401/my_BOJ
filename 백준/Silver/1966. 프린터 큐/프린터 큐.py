from collections import deque

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    lvl = deque(map(int, input().split()))
    lvl[M] = float(lvl[M])
    res = 0
    cnt = 0

    while lvl:
        l = lvl[0]
        maxV = max(lvl)
        if maxV == l: # 최우선
            cnt += 1

        else:
            lvl.append(l)
        
        if isinstance(l,float) and l == maxV:
            res = cnt
            break

        lvl.popleft()
        
    print(res)
