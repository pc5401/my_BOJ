import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    # 반지름^2
    half = N // 2
    R2 = half * half
    x = 0
    y = half - 1
    cnt = 0
    # 1/4분면 산책
    while x <= half and y >= 0:
        d2 = (x + 1) * (x + 1) + y * y
        if d2 <= R2:
            x += 1
        if d2 >= R2:
            y -= 1
        cnt += 1
    # 4분면 대칭
    return cnt * 4

def main():
    # 입력
    N = int(input().strip())
    # 풀이
    result = solve(N)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
