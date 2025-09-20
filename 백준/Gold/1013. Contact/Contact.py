import sys
import re
input = sys.stdin.readline

pat = re.compile(r'^(100+1+|01)+$')

def solve(T, arr):
    out = []
    for s in arr:
        out.append("YES" if pat.fullmatch(s) else "NO")
    return out

def main():
    # 입력
    T = int(input().strip())
    arr = [input().strip() for _ in range(T)]

    # 풀이
    result = solve(T, arr)

    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
