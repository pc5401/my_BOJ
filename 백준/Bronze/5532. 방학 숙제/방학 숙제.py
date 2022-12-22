l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
cnt = 0
while a > 0 or b > 0:
    a -= c
    b -= d
    cnt += 1

print(l-cnt)