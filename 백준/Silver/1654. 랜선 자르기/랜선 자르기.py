from collections import defaultdict
import sys
input = sys.stdin.readline

K, N = map(int,input().split())
lst = [int(input()) for _ in range(K)]

left, right = 1, max(lst) # zerodivision error 땜에 0 -> 1로

while left <= right:
    mid = left + (right - left) // 2
    cnt = 0
    for i in range(K):
        cnt += lst[i] // mid # 중간값으로 잘라보자.

    if N > cnt: # 랜선 길이를 줄이자.
        right = mid - 1
    else: # 랜선을 늘리자.
        left = mid + 1

    # print(f'left : {left}, right : {right}, mid : {mid}')

print(right)