N, M = map(int, input().split())
input_lst = list(map(int , input().split()))
arr = sorted(input_lst)

def back(lst:list):
    global N, M

    l = len(lst)
    if l == M:
        print(*lst)
        return

    for i in arr:
        if i in lst:
            continue
        if lst and lst[-1] > i:
            continue

        lst.append(i)
        back(lst)
        lst.pop()

back([])