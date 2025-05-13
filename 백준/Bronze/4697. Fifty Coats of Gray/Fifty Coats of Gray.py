import sys
import math
input = sys.stdin.readline

def solve(n, width, length, height, coverage, m, openings):
    area_per = 2 * (width * height + length * height) + (width * length)
    for w_o, h_o in openings:
        area_per -= w_o * h_o
    total_area = area_per * n
    return math.ceil(total_area / coverage)

def main():
    # 입력
    while True:
        n, w, l, h, a, m = map(int, input().split())
        if n == w == l == h == a == m == 0:
            break
        openings = [tuple(map(int, input().split())) for _ in range(m)]
        # 풀이
        result = solve(n, w, l, h, a, m, openings)
        # 출력
        print(result)

if __name__ == "__main__":
    main()
