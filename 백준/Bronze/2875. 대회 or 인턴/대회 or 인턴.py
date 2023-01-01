import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
n,m,k = N,M,K
cnt = 0

while 1:  # 인턴 고려 X 팀 수
    n -= 2
    m -= 1
    if n >= 0 and m >= 0:
        cnt += 1
    else:
        n += 2
        m += 1
        break

rm = n + m # remainer 남은 사람
res = 0
if rm - k >= 0:
    res = cnt
else:
    while 1:
        if rm - k >= 0:
            res = cnt
            break
        rm += 3
        cnt -= 1

print(res)
