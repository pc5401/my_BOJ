import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력값 처리
    N = int(input())
    A = list(map(int,input().split()))

    LIS = [A[0]]

    for i in range(1, N):
        if A[i] > LIS[-1]:
            LIS.append(A[i])
        else:
            lo, hi = 0, len(LIS)-1

            while lo < hi:
                mid = (lo+hi)//2
                if LIS[mid] < A[i]:
                    lo = mid + 1
                else:
                    hi = mid
            
            if lo == len(LIS):
                LIS.append(A[i])
            else:
                LIS[lo] = A[i]
        
    print(len(LIS))