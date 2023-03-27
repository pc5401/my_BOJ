import sys
input = sys.stdin.readline

def check(n):
    if n == 1:
        return True
    
    for i in range(2,n):
        if not n % i:
            return False
    return True

res = 0
str_V = input().rstrip()


for v in str_V:

    if v.isupper(): # 대문자
        res += (ord(v) - 38)
    else:
        res += (ord(v) - 96)

print('It is a prime word.'if check(res) else 'It is not a prime word.')