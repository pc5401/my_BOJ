import sys
input = sys.stdin.readline

def roman_to_int(s):
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    subs = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i, n = 0, len(s)
    total = 0
    while i < n:
        if i + 1 < n and s[i:i+2] in subs:
            total += subs[s[i:i+2]]
            i += 2
        else:
            total += vals[s[i]]
            i += 1
    return total

def int_to_roman(x):
    parts = [
        (1000,'M'), (900,'CM'), (500,'D'), (400,'CD'),
        (100,'C'), (90,'XC'), (50,'L'), (40,'XL'),
        (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')
    ]
    res = []
    for v, sym in parts:
        if x == 0: break
        q, x = divmod(x, v)
        if q:
            res.append(sym * q)
    return ''.join(res)

def solve(a_str, b_str):
    a = roman_to_int(a_str)
    b = roman_to_int(b_str)
    s = a + b
    return s, int_to_roman(s)

def main():
    # 입력
    A = input().strip()
    B = input().strip()

    # 풀이
    dec, rom = solve(A, B)

    # 출력
    print(dec)
    print(rom)

if __name__ == "__main__":
    main()
