import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

a,b = map(int,input().split())

if b > 9989899:
    b = 9989899
for i in range(a,b+1):
    v = str(i)
    if v == v[::-1] and is_prime(i):
        print(i)

print(-1)

