def calculate_area_polygon(n, points):
    
    area = 0
    
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2

if __name__ == '__main__':
    N = int(input().strip())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    area = calculate_area_polygon(N, points)
    print(round(area, 1))
