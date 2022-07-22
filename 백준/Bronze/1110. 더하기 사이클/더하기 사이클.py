N = n = int(input())
cnt = 0

while True:
    if n < 10:
        a = 0
        b = n
    else:
        a = n // 10
        b = n % 10

    v = a + b

    if v < 10:
        i = 0
        j = v
    else:
        i = v // 10
        j = v % 10

    n = b*10 + j

    cnt += 1
    if N == n:
        break

print(cnt)