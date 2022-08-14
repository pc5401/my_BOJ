N = int(input())
lst = list(map(int, input().split()))
Y = []
M = []

for i in range(N):
    v = lst[i]
    # 영식 요금
    y = (1 + v // 30) * 10
    Y.append(y)
    # 민식 요금
    m = (1 + v // 60) * 15
    M.append(m)

res = ''
if sum(Y) > sum(M):
    print('M', sum(M))
elif sum(Y) < sum(M):
    print('Y', sum(Y))
else:
    print('Y','M', sum(Y))
