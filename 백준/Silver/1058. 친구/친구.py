def func(idx):
    global res, N
    lst = [0]*N
    cnt = 0

    for i, v in enumerate(frd[idx]):
        if v == 'Y':
            lst[i] = 1
            for j, f in enumerate(frd[i]):
                if f == 'Y':
                    lst[j] = 1
    lst[idx] = 0
    cnt = sum(lst)
    res = max(res, cnt)


N = int(input())
frd = []
for _ in range(N):
    frd.append(list(input()))

res = 0

for i in range(N):
    func(i)

print(res)