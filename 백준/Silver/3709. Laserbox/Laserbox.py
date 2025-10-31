import sys

def solve(T, cases):
    res = []
    for n, r, gadgets, (sx, sy) in cases:
        gset = set(gadgets)
        if sy == 0:
            d = 0
        elif sy == n + 1:
            d = 2
        elif sx == 0:
            d = 1
        else:
            d = 3
        x, y = sx, sy
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        seen = set()
        while True:
            nx, ny = x + dx[d], y + dy[d]
            if nx == 0 or nx == n + 1 or ny == 0 or ny == n + 1:
                res.append(f"{nx} {ny}")
                break
            x, y = nx, ny
            state = (x, y, d)
            if state in seen:
                res.append("0 0")
                break
            seen.add(state)
            if (x, y) in gset:
                d = (d + 1) % 4
    return "\n".join(res)

def main():
    #입력
    input = sys.stdin.readline
    T = int(input().strip())
    cases = []
    for _ in range(T):
        n, r = map(int, input().split())
        gadgets = [tuple(map(int, input().split())) for _ in range(r)]
        sx, sy = map(int, input().split())
        cases.append((n, r, gadgets, (sx, sy)))
    #풀이
    ans = solve(T, cases)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
