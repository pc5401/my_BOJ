def func(number):
    lst.append(number)

    num = number % 10

    for i in range(10):
        if num > i:
            ni = number*10 + i
            func(ni)

N = int(input())
lst = []
for i in range(10):
    func(i)


ans = sorted(lst)
print(ans[N-1] if N <= len(lst) else -1)