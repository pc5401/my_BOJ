import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 강의수, 마일리지
lct = [0] * n

for tc in range(n):
    p, l = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    if p < l:
        lct[tc] = 1
    else: # 같거나 적거나.
        lct[tc] = lst[l-1] # 애랑 같아야함

lct.sort() # 정렬
cnt = 0
for v in lct:
    if m >= v:
        cnt += 1
        m -= v
    else:
        break

print(cnt)
