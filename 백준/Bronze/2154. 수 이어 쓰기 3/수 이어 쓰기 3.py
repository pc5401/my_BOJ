N = input()
l = len(N)
v = ''
res = 0
for i in range(1,int(N)+1):
    v += str(i)
for i in range(len(v)):
    if v[i:i+l] == N:
        res = i + 1
        break

print(res)