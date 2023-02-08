import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    yCnt, kCnt = 0, 0
    for n in range(9):
        y,k = map(int,input().split())
        yCnt += y
        kCnt += k
        
    res = "Draw"
    if yCnt > kCnt:
        res = "Yonsei"
    elif kCnt > yCnt:
        res = "Korea"
    print(res)