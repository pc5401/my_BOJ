a = input()
b = input()

alen = len(a)
blen = len(b)

dp = [[0] * (blen +1) for _ in range(alen + 1)]
maxV = 0

for i, A in enumerate(a):
    for j, B in enumerate(b):
        if A == B:
            dp[i+1][j+1] = dp[i][j] + 1
            if dp[i+1][j+1] > maxV:
                maxV = dp[i+1][j+1]

print(maxV)