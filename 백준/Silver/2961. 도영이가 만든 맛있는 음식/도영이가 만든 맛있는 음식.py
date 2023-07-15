import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력과 전처리
    N = int(input())
    lst = [list(map(int,input().split())) for i in range(N)]
    res = float('INF')
    for i in range(1, 1 << N):
        s, b = 1, 0
        for j in range(N):
            if (i & (1 << j)):
                s *= lst[j][0]
                b += lst[j][1]

        if abs(s-b) < res:
            res = abs(s-b)
    print(res)