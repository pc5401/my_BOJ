import sys

input = sys.stdin.readline
s = 0
while 1:
    n = int(input())
    if n == -1:
        print(s)
        break
    s += n