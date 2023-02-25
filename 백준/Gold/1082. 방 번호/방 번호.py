import sys
input = sys.stdin.readline

N = int(input())
input_list = list(map(int,input().split()))
M = int(input())
dp = [0] * (M+1)

def func(idx, money, value):
    x = dp[idx-money] # money 쓰지 않았을 때 최대값
    if x == 0:
        return value
    
    xlst = list(str(x))
    V = str(value)
    for e,l in enumerate(xlst):
        if l >= V:
            continue
        xlst.insert(e,V)
        return int("".join(xlst))
    
    return int("".join(xlst) + V)



lst = []
for i,l in enumerate(input_list):
    lst.append([l,i]) # l = 비용, i = 번호
lst.sort(key=lambda x :(x[0],-x[1])) # 비용이 싼 순으로 오름차순
if lst[0][1] == 0:
    l,i = lst[0][0], lst[0][1]
    lst.pop(0)
    lst.append([l,i])

for m, value in lst:
    for i in range(m,M+1):
        cal = func(i,m,value)
        dp[i] = max(dp[i], cal)

print(dp[M])
