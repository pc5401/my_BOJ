n = int(input())
if n % 10:
    print(-1)
    exit()

a = n // 300
n -= a*300
b = n // 60
n -= b*60
c = n // 10
n -= c * 10
print(a,b,c)