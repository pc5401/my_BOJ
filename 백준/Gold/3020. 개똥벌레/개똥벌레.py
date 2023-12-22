# 누적합 이용해서 풀이
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, H = map(int, input().split())
    bottom = [0] * (H+1) # 석순
    top = [0] * (H+1) # 종류석

    for i in range(N): # 높이별 DATA 처리
        h = int(input())
        if i % 2 == 0:
            bottom[h] += 1
        else:
            top[h] += 1

    for i in range(H-1, 0, -1): # 누적합
        bottom[i] += bottom[i+1]
        top[i] += top[i+1]
    
    minV = N
    cnt = 0
    for i in range(1, H+1): # 높이, 장애물 수
        value = bottom[i] + top[H-i+1]
        if value < minV:
            minV = value
            cnt = 1
        elif value == minV:
            cnt += 1
    
    print(minV, cnt)