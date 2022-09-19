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

        lst.append(i)
        back(lst)
        lst.pop()

back([])