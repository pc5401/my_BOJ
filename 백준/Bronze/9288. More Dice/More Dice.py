import sys
input = sys.stdin.readline

def solve(case_idx: int, s: int) -> str:
    lines = [f"Case {case_idx}:"]
    for a in range(1, 7):
        b = s - a
        if 1 <= b <= 6 and a <= b:
            lines.append(f"({a},{b})")
    return "\n".join(lines)

def main():
    # 입력
    T = int(input().strip())
    sums = [int(input().strip()) for _ in range(T)]
    # 풀이 & 출력
    for idx, s in enumerate(sums, start=1):
        print(solve(idx, s))

if __name__ == "__main__":
    main()
