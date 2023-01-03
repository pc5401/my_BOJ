import sys
input = sys.stdin.readline

N = int(input())
v = 1000 - N

coins = [500,100,50,10,5,1]
res = 0
idx = 0

while True:
    if v == 0:
        break

    cnt = v // coins[idx]

    if cnt:
        res += cnt

    v -= cnt * coins[idx]
    idx += 1

print(res)
