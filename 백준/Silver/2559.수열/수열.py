# 수열이라... 시간 초과의 압박이...(일단 실패)
# 처음은 for 문 돌리고 슬라이싱해서 sum함수로 합 구함(n^2)
# 구글링으로 해결 ㅠㅠ
import sys

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
maxi = 0

tmp = sum(lst[:k])
res = tmp

for i in range(k, n):
    tmp = tmp + lst[i] - lst[i-k] # 다음 꺼 넣고, 첫 번째 꺼 빼고
    res = max(res, tmp)  # max 함수로 크기 비교!

print(res)