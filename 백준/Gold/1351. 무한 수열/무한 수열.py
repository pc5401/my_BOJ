from collections import defaultdict
import sys
input = sys.stdin.readline

N, P, Q  = map(int,input().split())

def dp(n):

    if dic[n]:
        return dic[n]
    dic[n] = dp(n // P) + dp (n // Q)
    return dic[n]

dic = defaultdict(int)
dic[0] = 1
print(dp(N))