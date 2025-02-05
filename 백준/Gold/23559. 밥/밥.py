import sys
input = sys.stdin.readline

def solve(N, Z, menu):
    base_sum = sum(b for a, b in menu)
    diffs = []
    for a, b in menu:
        if a > b:
            diffs.append(a - b)

    K = (Z - 1000 * N) // 4000
    diffs.sort(reverse=True)
    extra_gain = sum(diffs[:min(K, len(diffs))])
    
    return base_sum + extra_gain


def main():
    # 입력
    N, Z = map(int, input().split())
    menu = [list(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(N, Z, menu)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()