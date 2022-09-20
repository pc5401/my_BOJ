N, M = map(int, input().split())
input_lst = list(map(int , input().split()))
arr = sorted(input_lst)

def back(lst:list, idx:int):
    global N, M

    l = len(lst)
    if l == M:
        print(*lst)
        return

    for i in range(idx,N):

        lst.append(arr[i])
        back(lst,i)
        lst.pop()

back([],0)