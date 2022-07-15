import sys
input = sys.stdin.readline

T = int(input()) 
for tc in range(T):
    N = int(input())  # 지원자 수
    l = []
    for n in range(N):
        x, y = map(int, input().split())
        l.append([x,y])

    lst = sorted(l)
    cnt = 1
    maxV = lst[0][1]
    for i in range(N):
        if maxV > lst[i][1]:
            cnt += 1
            maxV = lst[i][1]
    print(cnt)

