import sys
input = sys.stdin.readline

def func(n: int, lst: list):
    thr, two =  4, 8 * n - 12
    one = (N ** 2) * 5 - (thr * 3) - (two * 2)
    one_min = min(lst)
    
    two_min = 101
    for i,j in two_lst:
        two_min = min(two_min,lst[i]+lst[j])

    thr_min = 151
    for i,j,k in thr_lst:
        thr_min = min(thr_min, lst[i]+lst[j]+lst[k])

    res = one * one_min + two * two_min + thr * thr_min

    return res

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int,input().split()))
    thr_lst = ((0,1,2),(0,1,3),(0,2,4),(0,3,4),(1,2,5),(1,3,5),(2,4,5),(3,4,5)) # 8개
    two_lst = ((0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5))# 12
    if N == 1:
        print(sum(lst)-max(lst))
    else:
        print(func(N, lst))