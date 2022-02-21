# 일단 브루트포스로 해결하자.
first_num = int(input())
maxi = 0
maxi_lst = []


for second_num in range(first_num//2, first_num): # 모든 두번째 수를 상정한다.
    forth = first_num
    if forth == 1:
        back = 1
    else:
        back = second_num
    x = forth - back
    lst = [forth, back]
    cnt = 2
    while forth - back >= 0:
        x = forth - back
        lst.append(x)

        forth = back
        back = x
        cnt += 1

    if cnt > maxi:
        maxi = cnt
        maxi_lst = lst

print(maxi)
print(*maxi_lst)