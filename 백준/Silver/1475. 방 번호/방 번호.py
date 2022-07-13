import math
nums = list(input())

lst = [0]*9 # 0~8

for n in nums:
    v = int(n)

    if v == 9:
        v = 6

    lst[v] += 1

lst[6] = math.ceil(lst[6]/2)


print(max(lst))