import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = [float(input()) for _ in range(N)]
    res = [1] * N
    res[0] = lst[0]
    for i in range(1, N):
        if res[i-1] * lst[i] > lst[i]:
            res[i] =  res[i-1] * lst[i]
        else:
            res[i] = lst[i]

    print("{:.3f}".format(max(res)))
