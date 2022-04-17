N = int(input())
lst = [0] * (N+1)
maxV = 0
for n in range(N):
    t, p, = map(int, input().split())
    maxV = max(maxV, lst[n])

    if 0 <= n+t < N+1: # 범위 지정
        if maxV + p > lst[n+t]:
            lst[n+t] = maxV + p


print(max(lst))