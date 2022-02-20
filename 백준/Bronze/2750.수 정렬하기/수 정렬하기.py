#  bubble sort
n = int(input())
lst = []
for _ in range(n):
    num = int(input())
    lst.append(num)

for i in range(n):
    for j in range(n-1):
        if lst[j] > lst[j+1]:
            x = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = x

for _ in range(n):
    print(lst[_])