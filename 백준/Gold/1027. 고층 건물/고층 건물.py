import math

def solve():
    n = int(input())
    buildings = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    max_visible_count = 0

    for i in range(n):
        current_visible_count = 0
        min_slope_left = float('inf')
        for j in range(i - 1, -1, -1):
            slope = (buildings[i] - buildings[j]) / (i - j)

            current_slope = (buildings[j] - buildings[i]) / (j - i)

            if current_slope < min_slope_left:
                current_visible_count += 1
                min_slope_left = current_slope

        max_slope_right = float('-inf')
        for j in range(i + 1, n):
            current_slope = (buildings[j] - buildings[i]) / (j - i)

            if current_slope > max_slope_right:
                current_visible_count += 1
                max_slope_right = current_slope
        
        if current_visible_count > max_visible_count:
            max_visible_count = current_visible_count

    print(max_visible_count)

solve()