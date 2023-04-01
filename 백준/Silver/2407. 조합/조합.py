from collections import defaultdict
import sys
input = sys.stdin.readline

N, M  = map(int,input().split())

n, m = 1, 1
cnt = M
while cnt:
    n *= N
    N -= 1
    m *= M
    M -= 1
    cnt -= 1

print(n//m)