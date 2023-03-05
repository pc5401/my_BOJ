import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int,input().split())))
res = 0

for i in range(N):
    arr = lst[:i] + lst[i+1:]
    left, right = 0, len(arr) - 1
    
    while left < right:
        v = arr[left] + arr[right] # 합
        if v == lst[i]:
            res += 1
            break

        if v < lst[i]: # 투포인터
            left += 1 # 왼쪽 올리기 -> v를 증가
        else:
            right -= 1 # 오른쪽 내리기 -> v 감소
        
        # 왼쪽 오른족, 역전 되면 good 이 아니네? 다음 i로 go

print(res)