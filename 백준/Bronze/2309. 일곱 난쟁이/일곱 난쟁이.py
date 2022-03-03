lst = [int(input()) for _ in range(9)]

number = sum(lst) - 100

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == number:
            lst.remove(lst[j])  # j 먼저
            lst.remove(lst[i])
            break
    if len(lst) == 7:
        break
lst.sort()

for k in lst:  # 답 출력
    print(k)