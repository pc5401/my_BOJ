x = int(input())
n = 1

while not n*(n+1) >= 2*x and 2*x > n*(n-1):
    n += 1

total = n*(n+1)/2
diff = total - x

c = 1
p = n

while diff:
    diff -= 1
    c += 1
    p -= 1

if n % 2: # 홀수
    print(f'{c}/{p}')
else:
    print(f'{p}/{c}')