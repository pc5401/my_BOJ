n = int(input())

l = n - len(str(n))*9 if n - len(str(n))*9 > 0 else 0

for i in range(l,n+1):
    if i == n:
        print(0)
        break
    
    v = sum(map(int,str(i))) + i

    if v == n:
        print(i)
        break
    