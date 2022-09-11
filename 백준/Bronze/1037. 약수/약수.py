N = int(input())
input_lst = list(map(int,input().split()))
lst = sorted(input_lst)

res = lst[-1]

i = 0
flag = True
while flag:
    r = res * lst[i]
    flag = False
    i += 1

    for l in lst:
        if r % l: # 약수 아님
            flag = True
            break

print(r)