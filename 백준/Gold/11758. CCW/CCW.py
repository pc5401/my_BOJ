import sys
input = sys.stdin.readline

def CCW(a:tuple, b:tuple, c:tuple) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) -  (b[1] - a[1]) * (c[0] - a[0])


if __name__ == "__main__":
    ccw_res = CCW(*[tuple(map(int, input().split())) for _ in range(3)])

    if ccw_res > 0: 
        print(1)
    elif ccw_res < 0:
        print(-1)
    else:
        print(0)
