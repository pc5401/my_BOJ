tc = 1
while True:
    lst = list(map(int,input().split()))
    n = lst[0]
    if n == 0:
        break

    if n % 2: # 홀수
        v = float(lst[int(n/2)+1])
    else:
        v = (lst[n//2] + lst[n//2 + 1]) / 2

    print(f'Case {tc}: {v}')
    tc += 1

