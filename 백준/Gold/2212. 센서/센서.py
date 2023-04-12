import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
lst = sorted(list(map(int, input().split())))

if K >= N:  # K가 N보다 크거나 같은 경우, 모든 센서를 커버할 수 있음
    print(0)
else:
    res = lst[-1] - lst[0]
    k = K - 1
    l_lst = []

    for i in range(1, N):
        l_lst.append(lst[i] - lst[i - 1])

    l_lst.sort(key=lambda x: -x)

    while k:
        v = l_lst.pop(0)
        res -= v
        k -= 1

    print(res)