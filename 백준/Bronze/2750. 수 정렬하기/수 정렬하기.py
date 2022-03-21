#  selction sort
n = int(input())
lst = []
for _ in range(n):
    num = int(input())
    lst.append(num)

for i in range(n-1):  # 최소값을 찾고, 배치한 자리 제외하고 진행
    min_idx = i  # 최소값 저장소
    for j in range(i+1, n):
        if lst[min_idx] > lst[j]:
            min_idx = j
        else:
            pass
    lst[i], lst[min_idx] = lst[min_idx], lst[i]


for _ in range(n):
    print(lst[_])