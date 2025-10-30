import sys

def solve(N, M, Q, queries):
    Lx, Ux = 1, N
    Ly, Uy = 1, M
    for x, y, d in queries:
        if d == 1:
            if not (Ly <= y <= Uy): return 0
            Ly, Uy = y, y
            Lx = max(Lx, x + 1)
        elif d == 2:
            if not (Ly <= y <= Uy): return 0
            Ly, Uy = y, y
            Ux = min(Ux, x - 1)
        elif d == 3:
            if not (Lx <= x <= Ux): return 0
            Lx, Ux = x, x
            Uy = min(Uy, y - 1)
        elif d == 4:
            if not (Lx <= x <= Ux): return 0
            Lx, Ux = x, x
            Ly = max(Ly, y + 1)
        elif d == 5:
            Lx = max(Lx, x + 1)
            Ly = max(Ly, y + 1)
        elif d == 6:
            Ux = min(Ux, x - 1)
            Ly = max(Ly, y + 1)
        elif d == 7:
            Lx = max(Lx, x + 1)
            Uy = min(Uy, y - 1)
        elif d == 8:
            Ux = min(Ux, x - 1)
            Uy = min(Uy, y - 1)
        else:  # d == 9
            Lx, Ux = x, x
            Ly, Uy = y, y
        if Lx > Ux or Ly > Uy:
            return 0
    return (Ux - Lx + 1) * (Uy - Ly + 1)

def main():
    #입력
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Q = int(input())
    queries = [tuple(input().split()) for _ in range(Q)]
    queries = [(int(x), int(y), int(d)) for x, y, d in queries]
    #풀이
    ans = solve(N, M, Q, queries)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
