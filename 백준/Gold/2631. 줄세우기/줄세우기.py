N = int(input())
lst = [int(input()) for n in range(N)]
len_arr = [1] * N

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            len_arr[i] = max(len_arr[i], len_arr[j]+1)

res = max(len_arr)
print(N-res)