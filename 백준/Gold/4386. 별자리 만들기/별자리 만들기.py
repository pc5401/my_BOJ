import sys
import math
input = sys.stdin.readline


def create_star_link(n: int, start: list) -> list:
    rtn = []
    for i in range(N):
        for j in range(i, N):
            rtn.append([i, j, math.sqrt(abs(stars[i][0]- stars[j][0])**2 + abs(stars[i][1]- stars[j][1])**2)])

    return rtn


def find(x: int) -> int:
    if star_linked[x] != x:
        star_linked[x] = find(star_linked[x])
    return star_linked[x]


def union(x: int, y: int):
    X, Y = find(x), find(y)
    if X != Y:
        star_linked[X] = Y

if __name__ == '__main__':
    N = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(N)]

    star_linked = {i:i for i in range(N)}
    star_links = create_star_link(N, stars)
    star_links.sort(key=lambda x : x[2])

    res = 0.0
    
    for x, y, l in star_links:
        if find(x) != find(y):
            union(x, y)
            res += l

    print(round(res, 2))