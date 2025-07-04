import sys
input = sys.stdin.readline

def solve(n: int, cross: list[int], left: list[int], right: list[int]) -> tuple:
    leftCum = [0] * (n + 1)
    for i in range(2, n + 1):
        leftCum[i] = leftCum[i - 1] + left[i - 2]
    rightCum = [0] * (n + 2)
    for i in range(n - 1, 0, -1):
        rightCum[i] = rightCum[i + 1] + right[i - 1]
    best_i = 1
    best_dist = leftCum[1] + cross[0] + rightCum[1]
    for i in range(2, n + 1):
        dist = leftCum[i] + cross[i - 1] + rightCum[i]
        if dist < best_dist:
            best_dist = dist
            best_i = i
    return best_i, best_dist

def main():
    # 입력
    n = int(input().strip())
    cross = list(map(int, input().split()))
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    # 풀이
    idx, dist = solve(n, cross, left, right)
    # 출력
    print(idx, dist)

if __name__ == "__main__":
    main()
