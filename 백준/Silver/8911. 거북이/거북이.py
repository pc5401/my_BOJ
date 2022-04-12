T = int(input())
delta =[[1, 0], [0, 1], [-1, 0], [0, -1]]  # 동서남북
for tc in range(1, T+1):
    plsX = plsY = mnsX = mnsY = d = 0
    turtle = [0, 0]
    move = list(input())

    for m in move:
        if m == 'L':
            d = d - 1 if d - 1 >= 0 else 3

        elif m == 'R':
            d = d + 1 if d + 1 <= 3 else 0

        elif m == 'F':
            turtle[0] += delta[d][0]
            turtle[1] += delta[d][1]

        elif m == 'B':
            turtle[0] -= delta[d][0]
            turtle[1] -= delta[d][1]

        plsX = max(plsX, turtle[1])  # x좌표
        plsY = max(plsY, turtle[0])  # y좌표
        mnsX = min(mnsX, turtle[1])
        mnsY = min(mnsY, turtle[0])

    lenX = plsX - mnsX
    lenY = plsY - mnsY

    res = lenX * lenY
    print(res)