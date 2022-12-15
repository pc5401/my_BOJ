train = 0
res = 0
for tc in range(4):
    off, on = map(int,input().split())

    train -= off
    train += on

    res = max(res, train)

print(res)
