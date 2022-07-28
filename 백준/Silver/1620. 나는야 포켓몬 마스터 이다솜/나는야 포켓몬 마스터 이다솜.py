import sys
from collections import defaultdict
input = sys.stdin.readline


N, M = map(int, input().split())
lst = ['']
names = defaultdict(int)
for n in range(1, N+1):
    data = input().strip('\n')
    lst.append(data)
    names[data] = n

for m in range(M):
    data = input().strip('\n')
    if data.isdigit():
        print(lst[int(data)])
    else:
        print(names[data])

