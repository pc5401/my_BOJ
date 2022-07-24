res = 1
for _ in range(3):
    req = int(input())
    res *= req

lst = [0] * 10

while res:

    num = res % 10
    lst[num] += 1
    res = res // 10

for i in lst:
    print(i)