def lotto(lst:list,idx:int):
    global n

    if len(lst) >= 6:
        print(nums[lst[0]],nums[lst[1]],nums[lst[2]],nums[lst[3]],nums[lst[4]],nums[lst[5]])
        return

    for i in range(1,n+1):
        if idx >= i:
            continue

        lst.append(i)
        lotto(lst,i)
        lst.pop()


while 1:
    nums = list(map(int,input().split()))
    n = nums[0]

    if n == 0:
        break

    lotto([],0)
    print()

