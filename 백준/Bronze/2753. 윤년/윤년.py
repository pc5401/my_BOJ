n = int(input())

res = 0

if not n % 4:
    res = 1

if not n % 100:
    res = 0
    
if not n % 400:
    res = 1
print(res)