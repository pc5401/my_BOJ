n = int(input())

cnt = 2

while n > 1:
    if (n / cnt) % 1 == 0:
        print(cnt)
        n /= cnt
        cnt = 2

    else:
        cnt += 1
