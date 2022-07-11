t = int(input())
for _ in range(1, t+1):
    a, b = map(int, input().split())
    c = a+b
    print(f'Case #{_}: {a} + {b} = {c}')