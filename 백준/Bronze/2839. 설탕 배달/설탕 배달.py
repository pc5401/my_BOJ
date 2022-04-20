N =int(input())

cnt = 0

while N > 0:
    S, r = divmod(N, 5)
    if r:
        N -= 3
        cnt +=1
    else:
        cnt += S
        break

print(cnt if N >=0 else -1)