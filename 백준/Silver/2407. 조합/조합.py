from functools import lru_cache
import sys
input = sys.stdin.readline

N, M  = map(int,input().split())

@lru_cache(None)
def comb(n, m):
    if n == m or m == 0:
        return 1
    return comb(n-1, m-1) + comb(n-1, m)


print(comb(N,M))