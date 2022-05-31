def this_inner(x, y, cx, cy, r):
    dist = (x-cx)**2 + (y-cy)**2
    if r*r > dist:  # 행성계에 있음

        return 1
    else:
        return 0


T = int(input())
for tc in range(T):
    res = 0
    x1, y1, x2, y2 =map(int,input().split())
    n = int(input())

    for i in range(n):
        ans = 0
        cx, cy, r = map(int, input().split())
        ans += this_inner(x1, y1, cx, cy, r)
        ans += this_inner(x2, y2, cx, cy, r)

        if ans == 1:
            res += 1

    print(res)