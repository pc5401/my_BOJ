import sys

def solve(n, plats):
    plats.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        y, x1, x2 = plats[i]
        Lpos = 2 * x1 + 1
        Rpos = 2 * x2 - 1
        baseL = 0
        baseR = 0
        for j in range(i):
            yb, xb1, xb2 = plats[j]
            a = 2 * xb1
            b = 2 * xb2
            if a < Lpos < b:
                if yb > baseL:
                    baseL = yb
            if a < Rpos < b:
                if yb > baseR:
                    baseR = yb
        ans += (y - baseL) + (y - baseR)
    return ans

def main():
    #입력
    input = sys.stdin.readline
    n = int(input().strip())
    plats = [tuple(map(int, input().split())) for _ in range(n)]
    #풀이
    res = solve(n, plats)
    #출력
    print(res)

if __name__ == "__main__":
    main()
