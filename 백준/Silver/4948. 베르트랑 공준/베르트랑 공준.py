import sys
input = sys.stdin.readline

def func(num):

    n = len(lst)
    for i in range(num, n, num):
        lst[i] = 0
    lst[num] = 1


lst = [_ for _ in range(123457*2)]
lst[0] = lst[1] = 0

for l in lst:
    if l:
        func(l)

while 1:

    data = int(input())
    if not data:
        break
    start = data + 1
    end = 2*data +1
    print(sum(lst[start:end]))
