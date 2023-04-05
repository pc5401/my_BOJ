from collections import deque, defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    dic = defaultdict(list)
    for i in range(n+2):
        x,y = map(int,input().split())
        dic[i] = [x,y,i,0] # 좌표, 방문
    res = 'sad'
    Q = deque()
    Q.append(0)

    while Q:
        value = Q.popleft()
        v = dic[value]
        dic[v[2]][3] = 1

        if value == n+1:
            res = 'happy'
            break

        for i in range(1,n+2):
            if dic[i][3]:
                continue

            if abs(v[0] - dic[i][0]) + abs(v[1] - dic[i][1]) <= 1000:
                Q.append(i)
    # print(dic)
    print(res)