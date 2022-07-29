N = int(input())
res = []
for n in range(N):
    lst = list(map(str, input()))
    cnt = 0
    saver = 0
    for l in lst:
        if l == 'O':
            cnt += 1
            saver += cnt
        else:
            cnt = 0
            saver += cnt

    res.append(saver)

for r in res:
    print(r)
