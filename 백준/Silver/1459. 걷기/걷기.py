from collections import deque, defaultdict
import sys
input = sys.stdin.readline

X, Y, W, S = map(int,input().split())

if W > S:
    a = max(X,Y)
    print(a * S) if X % 2 == Y % 2 else print(a * S + (W-S))
else: # W < S
    a = max(X,Y)
    b = min(X,Y)
    print(min(a*W + b*W, (a-b) * W + b * S ))