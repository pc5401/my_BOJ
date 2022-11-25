N, Q = map(int,input().split())
lst = []

for i in range(1,N+1):
    n = int(input())
    for j in range(n):
        lst.append(i)
    
for i in range(Q):
    n = int(input())
    print(lst[n])
