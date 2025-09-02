import sys
input = sys.stdin.readline

def solve(N):
    if N == 1:
        return 1
    cnt = 0
    for d in range(9, 1, -1):
        while N % d == 0:
            N //= d
            cnt += 1
    return cnt if N == 1 else -1

def main():
    # 입력
    T = int(input().strip())
    nums = [int(input().strip()) for _ in range(T)]

    # 풀이
    result = [solve(n) for n in nums]

    # 출력
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
