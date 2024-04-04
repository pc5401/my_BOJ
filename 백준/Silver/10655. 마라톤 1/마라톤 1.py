import sys
input = sys.stdin.readline


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def solve(n, points):
    # 전체 경로의 기본 거리 계산
    total_distance = sum(manhattan_distance(points[i], points[i+1]) for i in range(n-1))
    
    # 건너뛰기로 인해 절약할 수 있는 최대 거리
    max_save = 0
    
    for i in range(1, n-1):
        distance_without_skip = manhattan_distance(points[i-1], points[i]) + manhattan_distance(points[i], points[i+1])
        distance_with_skip = manhattan_distance(points[i-1], points[i+1])
        save = distance_without_skip - distance_with_skip
        max_save = max(max_save, save)
    
    # 최소 거리는 전체 거리에서 절약할 수 있는 최대 거리를 뺀 것
    return total_distance - max_save


def main():
    # 입력값
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    # 풀이 후, 출력

    print(solve(N, points))


if __name__ == "__main__":
    main()
