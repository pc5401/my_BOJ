N, M = map(int, input().split())

def back(lst:list):
    global N, M

    l = len(lst)
    if l == M:
        print(*lst)
        return

    for i in range(1,N+1):
        if lst and lst[-1] > i:
            continue
        lst.append(i)
        back(lst)
        lst.pop()

back([])