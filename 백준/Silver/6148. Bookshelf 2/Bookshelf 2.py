import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력과 전처리
    N,B = map(int, input().split())
    lst = [int(input()) for i in range(N)]
    res = sum(lst) - B
    for i in range(1 << N):
        s = 0
        for j in range(N):
            if (i & (1 << j)):
                s += lst[j]

        if s >= B and s - B < res:
            res = s - B

    print(res)