import sys, math
input = sys.stdin.readline

# x1,y1 을 x2,y2 지나는 직선의 방정식 계수를 구하는 함수
def normalize_line(x1: int, y1: int, x2: int, y2: int) -> tuple:
    A = y2 - y1
    B = x1 - x2
    C = -(A * x1 + B * y1)
    g = math.gcd(math.gcd(abs(A), abs(B)), abs(C))
    if g != 0:
        A //= g
        B //= g
        C //= g
    # A와 B가 음수가 되지 않도록 조정 (A가 음수이거나 A가 0이고 B가 음수이면 부호 변경)
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return (A, B, C)

# 두 점의 파라미터 값(내적값)을 구하여 min, max 구간을 반환
def get_interval(x1: int, y1: int, x2: int, y2: int, dx: int, dy: int) -> tuple:
    t1 = dx * x1 + dy * y1
    t2 = dx * x2 + dy * y2
    return (min(t1, t2), max(t1, t2))

# 주어진 구간들이 몇 개의 병합된 구간으로 구성되는지를 구하는 함수
def merge_intervals(intervals: list) -> int:
    intervals.sort(key=lambda x: x[0])
    merged_count = 0
    if not intervals:
        return 0
    cur_start, cur_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= cur_end:  # 겹치거나 접하면 병합
            cur_end = max(cur_end, end)
        else:
            merged_count += 1
            cur_start, cur_end = start, end
    merged_count += 1
    return merged_count

def solve(N: int, segments: list[tuple[float, float, float, float]]) -> int:
    # 좌표를 정수로 처리하기 위해 100을 곱함
    seg_info = []
    for (x1, y1, x2, y2) in segments:
        ix1 = int(round(x1 * 100))
        iy1 = int(round(y1 * 100))
        ix2 = int(round(x2 * 100))
        iy2 = int(round(y2 * 100))
        line_key = normalize_line(ix1, iy1, ix2, iy2)
        seg_info.append((line_key, ix1, iy1, ix2, iy2))
    
    # 동일한 직선에 속하는 선분들을 그룹화
    groups = {}
    for key, ix1, iy1, ix2, iy2 in seg_info:
        if key not in groups:
            groups[key] = []
        groups[key].append((ix1, iy1, ix2, iy2))
    
    total_lines = 0
    for key, segs in groups.items():
        ix1, iy1, ix2, iy2 = segs[0]
        dx = ix2 - ix1
        dy = iy2 - iy1

        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy
        intervals = []
        # 각 선분에 대해 방향 벡터로 프로젝션한 구간을 구함
        for (x1, y1, x2, y2) in segs:
            interval = get_interval(x1, y1, x2, y2, dx, dy)
            intervals.append(interval)
        total_lines += merge_intervals(intervals)
    return total_lines

def main():
    # 입력
    N = int(input().strip())
    segments = []
    for _ in range(N):
        x1, y1, x2, y2 = map(float, input().split())
        segments.append((x1, y1, x2, y2))
    
    # 풀이
    result = solve(N, segments)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
