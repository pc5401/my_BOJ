import sys
input = sys.stdin.readline

def solve(expr: str) -> str:
    parts = expr.split()
    a = int(parts[0])
    b = int(parts[2])
    c = int(parts[4])
    return "YES" if a + b == c else "NO"

def main():
    expr = input().rstrip()
    result = solve(expr)
    print(result)

if __name__ == "__main__":
    main()
