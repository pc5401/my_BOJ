import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    M = 0
    p = 5
    while p <= N:
        M += N // p
        p *= 5
    return M

def main():
    # 입력
    case = 1
    while True:
        N = int(input().strip())
        if N == 0:
            break
        # 풀이
        result = solve(N)
        # 출력
        print(f"Case #{case}: {result}")
        case += 1

if __name__ == "__main__":
    main()
