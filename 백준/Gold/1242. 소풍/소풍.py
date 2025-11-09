import sys

def solve(n, k, m):
    pos = m
    t = 1
    s = n
    while s:
        r = (k - 1) % s + 1
        if pos == r:
            return t
        pos -= r
        if pos <= 0:
            pos += s
        t += 1
        s -= 1
    return t

def main():
    #입력
    input = sys.stdin.readline
    n, k, m = map(int, input().split())
    #풀이
    ans = solve(n, k, m)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
