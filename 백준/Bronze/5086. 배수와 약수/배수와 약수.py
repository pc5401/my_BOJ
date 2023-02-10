while 1:
    res = ""
    x,y = map(int,input().split())

    if x == y == 0:
        break


    if x > y and x % y == 0: #배수
        res = "multiple"

    elif x < y and y % x == 0: # 약수
        res = "factor"

    else:
        res = "neither"
    print(res)