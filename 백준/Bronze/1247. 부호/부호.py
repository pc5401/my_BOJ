import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    v= 0
    for n in range(N):
        v += int(input())
    
    if v > 0:
        print('+')
    elif v < 0:
        print('-')
    else:
        print('0')
