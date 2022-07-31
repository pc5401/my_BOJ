n = int(input())
n_len = len(str(n))
m = int(input())
if not m:
    print(min(n_len, abs(n -100)))
    quit()

ban = list(map(int, input().split()))

minV = abs(n -100)

for i in range(1000001):
    chk = str(i)
    flag =  1
    for j in chk:
        if int(j) in ban:
            flag = 0
            break
    if flag:
        i_len = len(str(i))
        minV = min(minV, abs(n-i)+i_len)

print(minV)