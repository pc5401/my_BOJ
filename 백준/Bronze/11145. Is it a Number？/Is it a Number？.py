import sys
input = sys.stdin.readline

def solve(T: int, cases: list[str]) -> list[str]:
    res = []
    for s in cases:
        s = s.strip()
        if not s or not s.isdigit():
            res.append("invalid input")
        else:
            res.append(str(int(s)))
    return res

def main():
    T = int(input().strip())
    cases = [input() for _ in range(T)]
    ans = solve(T, cases)
    print("\n".join(ans))

if __name__ == "__main__":
    main()
