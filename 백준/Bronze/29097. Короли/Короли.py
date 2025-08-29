import sys
input = sys.stdin.readline

def solve(n, m, k, a, b, c):
    totals = {
        "Joffrey": n * a,
        "Robb": m * b,
        "Stannis": k * c,
    }
    mx = max(totals.values())
    names = [name for name in ("Joffrey", "Robb", "Stannis") if totals[name] == mx]
    return " ".join(names)

def main():
    # 입력
    n, m, k, a, b, c = map(int, input().split())

    # 풀이
    result = solve(n, m, k, a, b, c)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
