lst = []
for i in range(1, 10000+1):
    number = n =  i
    while n:
        num = n % 10
        number += num
        n = n // 10
    lst.append(number)

for i in range(1, 10000+1):
    if not i in lst:
        print(i)