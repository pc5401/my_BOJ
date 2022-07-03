import sys

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    a,b = map(int, input().split())
    print(a+b)
