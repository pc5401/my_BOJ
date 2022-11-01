a, b = map(int,input().split())

x1, y1 = (a-1) // 4, (a-1) % 4
x2, y2 = (b-1) // 4, (b-1) % 4

x = abs(x1 - x2)
y = abs(y1 - y2)
print(x+y)