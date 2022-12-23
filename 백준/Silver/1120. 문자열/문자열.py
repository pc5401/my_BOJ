A, B  =input().split()
a = len(A)
b = len(B)

n = b - a
res = 100
for i in range(n+1):
    cnt = 0
    for j in range(a):
        if A[j] == B[j+i]:
            cnt += 1

    res = min(res, b - (cnt+n))

print(res)
