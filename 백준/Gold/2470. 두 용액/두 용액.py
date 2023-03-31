import sys
input = sys.stdin.readline
N = int(input())
input_lst = list(map(int,input().split()))
lst = sorted(input_lst)
s, e = 0, len(lst)-1
cnt = abs(lst[s] + lst[e])
res = [lst[s],lst[e]]

while s < e:
    v = lst[s] + lst[e]
    if cnt > abs(v):
        cnt = abs(v)
        res[0] = lst[s]
        res[1] = lst[e]

    if cnt == 0:
        break

    if v < 0: # 음수
        s += 1
    else: # 양수
        e -= 1
    
print(*res)