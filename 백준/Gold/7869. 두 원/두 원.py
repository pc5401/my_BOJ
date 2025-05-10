import sys, math
input = sys.stdin.readline

def solve(x1: float, y1: float, r1: float,
          x2: float, y2: float, r2: float) -> float:
    dx = x1 - x2
    dy = y1 - y2
    d = math.hypot(dx, dy)
    
    # 전혀 겹치지 않을 때
    if d >= r1 + r2:
        return 0.0
            
    # 한 원이 다른 원 안에 완전히 포함될 때
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2

    # 코사인 법칙에 의한 각 계산
    cos1 = (d*d + r1*r1 - r2*r2) / (2 * d * r1)
    cos2 = (d*d + r2*r2 - r1*r1) / (2 * d * r2)
    cos1 = max(-1.0, min(1.0, cos1))
    cos2 = max(-1.0, min(1.0, cos2))
    theta1 = math.acos(cos1)
    theta2 = math.acos(cos2)
    # 두 부채꼴 넓이의 합
    area1 = r1*r1 * theta1
    area2 = r2*r2 * theta2
    # 삼각형 두 개의 넓이 합
    area3 = 0.5 * math.sqrt(
        max(0.0, (-d+r1+r2)*(d+r1-r2)*(d-r1+r2)*(d+r1+r2))
    )
    return area1 + area2 - area3

def main():
    # 입력
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    # 풀이
    result = solve(x1, y1, r1, x2, y2, r2)
    # 출력
    print(f"{result:.3f}")

if __name__ == "__main__":
    main()
