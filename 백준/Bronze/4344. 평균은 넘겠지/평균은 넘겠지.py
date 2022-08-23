C = int(input())

res = []
for _ in range(C):
    a = list(map(int, input().split()))
    aver = sum(a[1:]) / a[0]
    cnt = 0
    for i in a[1:]:
        if i > aver:
            cnt += 1
    res.append(cnt/a[0])


for r in res:
    print(f'{r:.3%}')

    