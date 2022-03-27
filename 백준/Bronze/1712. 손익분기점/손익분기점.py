A, B, C = map(int, input().split())
ans = int(A/(C-B))+1 if C - B > 0 else -1
print(ans)