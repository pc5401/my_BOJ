import sys
import bisect
input = sys.stdin.readline

def get_LIS() -> list:
    """ last idx 역추적하여 LIS 출력
    Return:
        (list) : LIS 값
    """
    rtn = []
    idx = idx_map[len(LIS) - 1]
    while idx >= 0:
        rtn.append(line[idx])
        idx = prev[idx]

    return rtn[::-1]


if __name__ == "__main__": # LIS 이분탐색 + 실제 부분 수열 찾기
    # 입력값 처리
    N = int(input())
    line = list(map(int,input().split()))
    
    # 데이터 전처리, 시작값 세팅
    LIS = [line[0]]
    prev = [-1] * N
    idx_map = {0:0}

    for i in range(1, N):
        if line[i] > LIS[-1]: # LIS 추가
            prev[i] = idx_map[len(LIS) - 1]
            LIS.append(line[i])
            idx_map[len(LIS) - 1] = i
        else: # 이분탐색
            lo = bisect.bisect_left(LIS, line[i])
            LIS[lo] = line[i]
            idx_map[lo] = i
            if lo > 0:
                prev[i] = idx_map[lo-1]

    print(len(LIS))
    print(*get_LIS())