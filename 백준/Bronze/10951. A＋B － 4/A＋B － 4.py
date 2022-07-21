lst = []
while 1:
    try:
        a, b = map(int, input().split())
        lst.append(a+b)
    except:
        break

print(*lst)