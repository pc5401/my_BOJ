def func(n, m, lst):
    if len(lst) >= m:
        return print(*lst)

    for i in range(1, n+1):
        if not i in lst:
            func(n, m, lst + [i])




n, m = map(int, input().split())

func(n, m, [])