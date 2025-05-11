import sys
input = sys.stdin.readline

def solve(A: tuple[int,int], B: tuple[int,int], C: tuple[int,int], trees: list[tuple[int,int]]) -> tuple[float,int]:
    # 삼각형 전체 넓이
    xA,yA = A
    xB,yB = B
    xC,yC = C
    area2 = abs(xA*(yB-yC) + xB*(yC-yA) + xC*(yA-yB))
    area = area2 / 2.0

    def cross(p1, p2, p3):
        # (p2 - p1) x (p3 - p1)
        return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

    count = 0
    for P in trees:
        c1 = cross(A, B, P)
        c2 = cross(B, C, P)
        c3 = cross(C, A, P)
        # 모두 같은 부호이거나 0 이면 내부 또는 경계
        if (c1 >= 0 and c2 >= 0 and c3 >= 0) or (c1 <= 0 and c2 <= 0 and c3 <= 0):
            count += 1

    return area, count

def main():
    # 입력
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))
    N = int(input())
    trees = [tuple(map(int, input().split())) for _ in range(N)]
    # 풀이
    area, result = solve(A, B, C, trees)
    # 출력
    print(f"{area:.1f}")
    print(result)

if __name__ == "__main__":
    main()
