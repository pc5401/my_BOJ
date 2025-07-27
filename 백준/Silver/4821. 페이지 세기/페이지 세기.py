import sys
input = sys.stdin.readline

def solve(N: int, ranges: str) -> int:
    printed = [False] * (N + 1)
    parts = ranges.strip().split(',')
    for part in parts:
        if '-' in part:
            low_s, high_s = part.split('-')
            low, high = int(low_s), int(high_s)
        else:
            low = high = int(part)
        if low > high:
            continue
        # 문서 범위로 클리핑
        if high < 1 or low > N:
            continue
        low = max(low, 1)
        high = min(high, N)
        for p in range(low, high + 1):
            printed[p] = True

    return sum(printed[1:])

def main():
    results = []
    while True:
        # 입력
        line = input().strip()
        if line == '0':
            break
        N = int(line)
        ranges = input()
        # 풀이
        cnt = solve(N, ranges)
        results.append(str(cnt))
    # 출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
