A, B = map(int, input().split())
qns = int(input())

a, b = divmod(qns, 60)


ans = A + a if 24 >= A + a else (A + a) - 24
res = B + b

if res >= 60:
    res -= 60
    ans += 1
    
ans = ans if 24 > ans else ans - 24
print(ans, res)