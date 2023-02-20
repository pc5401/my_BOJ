import sys
input = sys.stdin.readline

L,R = input().split()
lenL, lenR = len(L), len(R)
cnt = 0
if lenL == lenR:
    for i in range(lenL):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break
print(cnt)
