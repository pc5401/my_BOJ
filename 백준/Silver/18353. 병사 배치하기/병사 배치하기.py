import sys
input = sys.stdin.readline

if __name__ == "__main__": # LIS 이분탐색
    N = int(input())
    lst = list(map(int,input().split()))
    LIS = []
    for i in range(N):
        if LIS and LIS[-1] > lst[i]:
            LIS.append(lst[i])
        else: # 이분탐색
            lo, hi = 0, len(LIS)

            while lo < hi:
                mid = (lo+hi) // 2
                if lst[i] >= LIS[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            
            if lo == len(LIS):
                LIS.append(lst[i])
            else:
                LIS[lo] = lst[i]

    print(N - len(LIS))