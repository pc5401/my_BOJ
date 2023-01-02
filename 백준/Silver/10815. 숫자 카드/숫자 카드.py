import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
lst = list(map(int,input().split()))
res = [0] * M

M_lst = []
for i, v in enumerate(lst):
    M_lst.append((v,i)) # [0] 값, [1] 인덱스


N_lst.sort()  # 가지고 있는 카드들
M_lst.sort(key=lambda x : x[0])  # 확인해야할 카드들

x = 0
y = 0

while True:
    if x >= N or y >= M:
        break

    if M_lst[y][0] > N_lst[x]:
        x += 1

    elif  M_lst[y][0] == N_lst[x]:
        res[M_lst[y][1]] = 1
        y += 1

    else:
        y += 1


print(*res)