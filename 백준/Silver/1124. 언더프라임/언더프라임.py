A, B = map(int,input().split())
nums = [1] * 100001
sosu = []

nums[0],nums[1] = 0, 0

for i in range(100001):
    if nums[i]:
        sosu.append(i)
        for j in range(i,100001,i):
            nums[j] = 0

def cal(v):
    n = v
    cnt = 0

    for s in sosu:
        if cnt > v or n <= 1:
            break

        while n >= 1:   
            if n % s == 0:
                cnt += 1
                n = n // s

            else:

                break


    if cnt in sosu:
        return 1
    else:
        return 0
    

res = 0
for i in range(A,B+1):
    res += cal(i)

print(res)