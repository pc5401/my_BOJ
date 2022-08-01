x, y, w, h = map(int, input().split())

i = min(x, w-x)
j = min(y, h-y)
print(min(i, j))