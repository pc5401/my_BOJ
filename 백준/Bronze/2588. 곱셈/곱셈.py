v = int(input())
n = int(input())

n1 = n % 10
n2 = (n // 10) % 10
n3 = (n // 100) % 10

print(v * n1)
print(v * n2)
print(v * n3)
print(v * n)
