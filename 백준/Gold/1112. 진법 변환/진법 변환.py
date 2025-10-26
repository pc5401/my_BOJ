import sys

def solve(x, b):
    if x == 0:
        return "0"
    if b > 0:
        sign = "-" if x < 0 else ""
        n = abs(x)
        digits = []
        while n:
            digits.append(str(n % b))
            n //= b
        return sign + "".join(reversed(digits))
    else:
        digits = []
        n = x
        while n != 0:
            n, r = divmod(n, b)
            if r < 0:
                n += 1
                r -= b
            digits.append(str(r))
        return "".join(reversed(digits))

def main():
    #입력
    x_str, b_str = sys.stdin.readline().split()
    x = int(x_str); b = int(b_str)
    #풀이
    ans = solve(x, b)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
