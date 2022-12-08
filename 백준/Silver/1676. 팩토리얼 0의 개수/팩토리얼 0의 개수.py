N = int(input())
v = 1
for i in range(1,N+1):
    v *= i

str_v = str(v)[::-1]
cnt = 0
for i in str_v:
    if i != '0':
        break
    cnt += 1

print(cnt)
