import sys
input = sys.stdin.readline

N, M = map(int, input().split())
input_lst = list(map(int, input().split()))
input_len = len(input_lst)

lst = [0] * input_len
lst[0] = input_lst[0]
for i in range(1, input_len):
    lst[i] = lst[i-1] + input_lst[i]

res = []
for _ in range(M):
    x, y = map(int, input().split())
    x = x-1
    y = y-1
    if x:
        res.append(lst[y]-lst[x-1] if y - x else input_lst[y])
    else:
        res.append(lst[y])

for result in res:
    print(result) 
