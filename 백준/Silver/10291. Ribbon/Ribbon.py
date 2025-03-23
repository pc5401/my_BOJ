import sys
input = sys.stdin.readline

def solve(n: int, ribbons: list[int]) -> (int, int):
    eff = [r - 2 for r in ribbons]
    max_eff = max(eff)
    
    best_total = -1
    best_L = 0
    best_count = 0

    for L in range(1, max_eff + 1):
        total_count = 0
        for length in eff:
            total_count += length // L
        total = L * total_count

        if total > best_total or (total == best_total and L > best_L):
            best_total = total
            best_L = L
            best_count = total_count
    return best_L, best_count

def main():
    # 입력
    lines = sys.stdin.read().strip().splitlines()
    results = []
    for line in lines:
        if not line.strip():
            continue
        parts = list(map(int, line.split()))
        n = parts[0]
        ribbons = parts[1:]
        L, count = solve(n, ribbons)
        results.append(f"{L} {count}")
    # 출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
