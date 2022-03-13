import itertools

n, m = map(int, input().split())
home = []
chicken = []
arr = []

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 1:
            home.append([i, j])
        elif lst[j] == 2:
            chicken.append([i, j])
        else:
            pass
    arr.append(lst)

#  치킨목록
chk_lst = list(map(list, itertools.combinations(chicken, m)))

res = 1e10
for chk in chk_lst:
    #  가장 가까운 치킨집 합
    sum_load = 0
    for i in home:
        # 가장 가까운 치킨집 거리
        chk_load = 1e10
        for j in chk:
            load = abs(i[0]-j[0])+ abs(i[1]-j[1])
            chk_load = min(chk_load, load)
        # sum에 계속 더하기
        sum_load += chk_load

        if sum_load > res:
            break

    res = min(res, sum_load)

print(res)