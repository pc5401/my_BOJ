import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    if N % 2 == 0 or N % 5 == 0:
        return -1
    rem = 0
    for length in range(1, N + 1):
        rem = (rem * 10 + 1) % N
        if rem == 0:
            return length
    return -1

def main():
    # 입력
    N = int(input())

    # 풀이
    result = solve(N)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
