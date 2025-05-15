import sys

def solve(N: int) -> int:
    return N * (N - 1) + 1

def main():
    # 입력
    for line in sys.stdin:
        N = int(line.strip())
        if N == 0:
            break
        # 풀이
        result = solve(N)
        # 출력
        print(f"{N} => {result}")

if __name__ == "__main__":
    main()
