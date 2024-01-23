import sys
input = sys.stdin.readline

if __name__ == "__main__": # LIS 이분탐색
    N = int(input())
    line = list(map(int,input().split()))
    LIS = []

    for i in range(N):
        if LIS and line[i] > LIS[-1]:
            LIS.append(line[i])
        else:
            lo, hi = 0, len(LIS)

            while lo < hi:
                mid = (lo+hi) // 2
                if line[i] > LIS[mid]:
                    lo = mid + 1
                else:
                    hi = mid

            if lo == len(LIS):
                LIS.append(line[i])
            else:
                LIS[lo] = line[i]
        
    print(len(LIS))