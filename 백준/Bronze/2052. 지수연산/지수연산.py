n = int(input())
v = "%.300f" % 2 ** -n
l = len(v)
for i in range(l-1, 1, -1):
    if v[i] != '0':
        l = i
        break
print(v[:l+1])