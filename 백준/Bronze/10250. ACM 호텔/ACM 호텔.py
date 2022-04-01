T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    x, y = divmod(N, H)

    # 호텔 호수로 바꾸기
    if y == 0:
        y = H
        x = '0' + str(x) if 10 > x else str(x)
    else:
        x = '0' + str(x + 1) if 9 > x else str(x + 1)

    print(str(y) + x)
