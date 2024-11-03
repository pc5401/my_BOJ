import sys
import math
from collections import defaultdict

input = sys.stdin.readline

def readints():
    return list(map(int, sys.stdin.readline().split()))

def normalize(dx, dy):
    if dx == 0 and dy == 0:
        return (0, 0)
    g = math.gcd(dx, dy)
    dx_norm = dx // g
    dy_norm = dy // g
    if dx_norm < 0 or (dx_norm == 0 and dy_norm < 0):
        dx_norm *= -1
        dy_norm *= -1
    return (dx_norm, dy_norm)

def solve(N, points):
    rtn = 0
    for i in range(N):
        A = points[i]
        freq = defaultdict(int)
        for j in range(N):
            if i == j:
                continue
            B = points[j]
            dx = B[0] - A[0]
            dy = B[1] - A[1]
            direction = normalize(dx, dy)
            freq[direction] += 1

        for (dx, dy), count in freq.items():
            perp1 = normalize(-dy, dx)
            count_perp = freq.get(perp1, 0)
            rtn += count * count_perp

    return rtn // 2


if __name__ == "__main__":
    # 입력값
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    # 풀이
    result = solve(N, points)

    # 출력
    print(result)