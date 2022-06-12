S = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sorted(A)
b = sorted(B, reverse=True)

res = 0
for i in range(S):
    res += a[i]*b[i]

print(res)