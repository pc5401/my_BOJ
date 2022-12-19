n = int(input())
res = []
for i in range(1, 2*n):
    if n >= i:
        a = '*' * i + ' ' * (n-i)
        b = ' '*(n-i) + '*' * i
    else:
        a = '*' * (n + (n-i)) + ' ' * abs(n-i)
        b = ' ' * abs(n-i) + '*' * (n+(n-i))
    res.append(a+b)
for r in res:
    print(r)