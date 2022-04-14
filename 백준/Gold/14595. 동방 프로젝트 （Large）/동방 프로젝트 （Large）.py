import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [0]*(N+1)
for i in range(M): # 벽 가르기
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] -= 1
    # 이렇게 만들면 스타트 [0, 1, 1, -1, -1, 1, 0, 0, -1, 0, 0 ] 으로 나옴
    # 그럼, 순회하면서 값을 더해가면, +n, -n 이 같아지는 순간(n-n=0)으로 방으로 구별된다.
    # 구분합이다.

ans = 0
for i in range(1, N+1): # 두 번째 인덱스 부터
    arr[i] += arr[i-1] # 이렇게 하면 합을 가지고 이동
    if arr[i] == 0: # 방이 닦힘
        ans += 1

print(ans)