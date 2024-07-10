import sys
input = sys.stdin.readline


def solve(n: int, d: int) -> int:
    start = 10**(n-1)
    if start % d == 0:
        return start
    else:
        val = start % d
        result = start + (d - val)
        
        if len(str(result)) == n:
            return result
        else:
            return "No solution"

def main():
    # 입력값
    n, d = map(int, input().split())
    # 풀이
    result: int = solve(n, d)
    # 출력
    print(result)


if __name__ == "__main__":
    main()