import sys
input = sys.stdin.readline

def solve(Xs: int, Ys: int, Xe: int, Ye: int, dx: int, dy: int) -> tuple[int, int]:
    if dx == 0 and dy == 0:
        return (Xe, Ye)
    
    top = (Xs - Xe) * dx + (Ys - Ye) * dy
    btm= dx * dx + dy * dy

    t = top / btm
    if t < 0:
        return (Xe, Ye)
    
    x = Xe + dx * t
    y = Ye + dy * t

    return (int(round(x)), int(round(y)))

def main():
    # 입력
    Xs, Ys = map(int, input().split())
    Xe, Ye, dx, dy = map(int, input().split())

    # 풀이
    result = solve(Xs, Ys, Xe, Ye, dx, dy)

    # 출력
    print(*result)

if __name__ == "__main__":
    main()

    