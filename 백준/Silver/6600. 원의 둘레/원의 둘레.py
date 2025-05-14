import sys
import math

def solve(x1, y1, x2, y2, x3, y3):
    a = math.hypot(x2 - x3, y2 - y3)
    b = math.hypot(x3 - x1, y3 - y1)
    c = math.hypot(x1 - x2, y1 - y2)
    
    area = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2
    R = a * b * c / (4 * area)
    return 2 * math.pi * R

def main():
    # 입력
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        x1, y1, x2, y2, x3, y3 = map(float, parts)
        # 풀이
        result = solve(x1, y1, x2, y2, x3, y3)
        # 출력
        print(f"{result:.2f}")

if __name__ == "__main__":
    main()
