code = input()
lst = []
cnt = 0
for c in code:
    if c == 'X':
        cnt += 1
    else:  # . 을 만나면
        if cnt:
            lst.append(cnt)
            cnt = 0
        lst.append(0)
if cnt:
    lst.append(cnt)

res = ''
for l in lst:
    v = l
    if l:
        a = v // 4
        v -= a*4
        b = v // 2
        v -= b*2

        if v:
            res = -1
            break

        res += 'AAAA'*a
        res += 'BB'*b

    else:
        res +='.'

print(res)
