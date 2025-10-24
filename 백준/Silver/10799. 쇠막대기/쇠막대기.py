import sys

def solve(s):
    ans = 0
    opened = 0
    prev = ''
    for ch in s.strip():
        if ch == '(':
            opened += 1
            prev = '('
        else:
            opened -= 1
            if prev == '(':
                ans += opened
            else:
                ans += 1
            prev = ')'
    return ans

def main():
    #입력
    s = sys.stdin.readline().strip()
    #풀이
    result = solve(s)
    #출력
    print(result)

if __name__ == "__main__":
    main()
