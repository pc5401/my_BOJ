import sys
input = sys.stdin.readline

def func(idx):
    cnt = 0
    for i in range(idx, 0, -1):
        if lst[i] <= lst[i-1]:
            v = lst[i-1] - lst[i] + 1
            cnt += v
            lst[i-1] -= v

    return cnt


if __name__ == "__main__":
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    res = 0
    for i in range(1,N):
        if lst[i] <= lst[i-1]:
            res += func(i)

    print(res)