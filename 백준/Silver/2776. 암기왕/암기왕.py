import sys
input = sys.stdin.readline

def cal(lst:list[int], target:int):
    global N
    start, end = 0, N-1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] > target: 
            end = mid - 1

        elif lst[mid] < target:
            start = mid + 1
        else:
            break

    if lst[mid] == target:
        return 1
    else:
        return 0


T = int(input())
for tc in range(T):
    N = int(input())
    lst1 = list(map(int,input().split()))
    M = int(input())
    lst2 = list(map(int,input().split()))
    lst1.sort()
    for i in lst2:
        print(cal(lst1,i))
