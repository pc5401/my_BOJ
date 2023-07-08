import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for i in range(N)]

if lst[2] - lst[1] == lst[1] - lst[0]: # 등차
    v = lst[1] - lst[0]
    print(lst[-1] + v)
else: #등비
    v = lst[1] // lst[0]
    print(lst[-1]*v)