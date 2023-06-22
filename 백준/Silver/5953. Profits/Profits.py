import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    # 누적합
    nowV = maxV = lst[0]

    for i in range(1,N):
        nowV = max(lst[i], nowV + lst[i])
        if nowV > maxV:
            maxV = nowV

    print(maxV)