import sys
import bisect
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    lines.sort() # 정렬

    # 데이터 전처리, 시작값 세팅
    LIS = [lines[0][1]]

    for i in range(1, N):
        if lines[i][1] > LIS[-1]: # LIS 추가
            LIS.append(lines[i][1])

        else:
            lo = bisect.bisect_left(LIS, lines[i][1])
            LIS[lo] = lines[i][1]

    print(len(LIS))