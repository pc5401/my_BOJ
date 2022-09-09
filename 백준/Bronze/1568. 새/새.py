N = int(input())

n = N
result = 0

while n:
    i = 1
    while True:
        v = (i * (1 + i))//2
        if n < v:
            result += i -1
            n -= (i*(i-1)) // 2
            break
        elif n == v:
            result += i
            n -= v
            break
        i += 1
print(result)