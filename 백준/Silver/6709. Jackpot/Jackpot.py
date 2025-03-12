import sys, math
input = sys.stdin.readline

def solve(w: int, periods: list[int]) -> str:
    lcm_val = periods[0]
    for p in periods[1:]:
        lcm_val = (lcm_val * p) // math.gcd(lcm_val, p)
        if lcm_val > 10**9:
            return "More than a billion."
    return str(lcm_val)

def main():
    # 입력
    n = int(input().strip())
    ans = []
    for _ in range(n):
        w = int(input().strip())
        periods = list(map(int, input().split()))
        # 풀이
        ans.append(solve(w, periods))
    # 출력
    print("\n".join(ans))

if __name__ == "__main__":
    main()
