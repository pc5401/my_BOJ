def hansu(n):
    cnt = 0
    for i in range(1, n+1):
        if i < 100:
            cnt +=1
            continue

        else:
            num = str(i)
            gap = int(num[-2]) -int(num[-1])
            flag = 0
            for j in range(1, len(num)):
                a = int(num[-j-1])
                b = int(num[-j])
                if a - b == gap:
                    pass
                else:
                    flag = 1
                    break
            cnt = cnt  if flag == 1 else cnt + 1

    return cnt


N = int(input())
ans = hansu(N)
print(ans)