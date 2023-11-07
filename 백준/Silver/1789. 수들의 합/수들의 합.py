N = int(input())
n = 1
res = 0

while 1 :
    if N - (n*(n+1)/2) == 0:
        break
    elif  N - (n*(n+1)/2) < 0:
        n -= 1
        break
    
    n += 1
print(n)

