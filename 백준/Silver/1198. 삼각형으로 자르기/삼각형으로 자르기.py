import sys
input = sys.stdin.readline

def solve(points):
    n = len(points)
    def area2(a, b, c):
        return abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]))
    best2 = 0
    for i in range(n):
        ai = points[i]
        for j in range(i+1, n):
            aj = points[j]
            for k in range(j+1, n):
                ak = points[k]
                a2 = area2(ai, aj, ak)
                if a2 > best2:
                    best2 = a2
    return best2 / 2.0

def main():
    # 입력
    N = int(input().strip())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    # 풀이
    ans = solve(pts)

    # 출력
    s = f"{ans:.10f}".rstrip('0').rstrip('.')
    print(s)

if __name__ == "__main__":
    main()
