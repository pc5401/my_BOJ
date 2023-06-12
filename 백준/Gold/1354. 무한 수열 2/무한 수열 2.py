import collections
import sys
input = sys.stdin.readline

N, P, Q, X, Y = map(int,input().split())


def dp(n):

    if dic[n]:
        return dic[n]
    x_idx, y_idx = (n // P) - X, (n // Q) - Y
    dic[n] = dp(x_idx if x_idx > 0 else 0) + dp (y_idx if y_idx > 0 else 0)
    return dic[n]

dic = collections.defaultdict(int)
dic[0] = 1
print(dp(N))