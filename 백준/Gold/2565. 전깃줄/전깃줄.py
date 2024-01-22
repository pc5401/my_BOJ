if __name__ == "__main__": # LIS 이분탐색
    N = int(input())
    line = [tuple(map(int,input().split())) for _ in range(N)]
    line.sort(key=lambda x: x[0])
    LIS = []

    for i in range(N):
        if LIS and LIS[-1] < line[i][1]:
            LIS.append(line[i][1])
        else: # 이분탐색
            lo, hi = 0, len(LIS)

            while lo < hi:
                mid = (lo+hi) // 2
                if line[i][1] > LIS[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            
            if lo == len(LIS):
                LIS.append(line[i][1])
            else:
                LIS[lo] = line[i][1]

    print(N - len(LIS))