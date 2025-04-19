import sys
input = sys.stdin.readline

def solve(points: list[tuple[int, int]]) -> bool:
    xs = sorted({x for x, y in points})
    ys = sorted({y for x, y in points})

    if len(xs) != 2 or len(ys) != 2:
        return False
    
    dx = xs[1] - xs[0]
    dy = ys[1] - ys[0]

    if dx != dy or dx == 0:
        return False

    required = {(xs[0], ys[0]), (xs[0], ys[1]), (xs[1], ys[0]), (xs[1], ys[1])}
    return set(points) == required

def main():
    # 입력
    points = [tuple(map(int, input().split())) for _ in range(4)]
    # 풀이
    is_square = solve(points)
    # 출력
    print("TAK" if is_square else "NIE")

if __name__ == "__main__":
    main()
