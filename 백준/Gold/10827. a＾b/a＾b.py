import sys
input = sys.stdin.readline

def solve(a_str, b):
    a_str = a_str.strip()
    int_part, frac_part = a_str.split('.')
    d = len(frac_part)
    A = int(int_part + frac_part)
    x = pow(A, b)
    k = d * b
    s = str(x)
    if k >= len(s):
        return "0." + "0" * (k - len(s)) + s
    else:
        return s[:-k] + "." + s[-k:]

def main():
    # 입력
    a_str, b_str = input().split()
    b = int(b_str)

    # 풀이
    result = solve(a_str, b)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
