import sys
import bisect
input = sys.stdin.readline



if __name__ == "__main__":
    # 입력값 처리
    N = int(input())
    A = list(map(int,input().split()))
    M = int(input())
    lst = list(map(int,input().split()))
    # 데이터 전처리
    A.sort()
    res = []
    
    for v in lst:
        lo = bisect.bisect_left(A, v)
        if lo < N and A[lo] == v:
            res.append(1)
        else:
            res.append(0)

    for r in res:
        print(r)