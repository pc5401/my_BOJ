import sys
input = sys.stdin.readline

def solve(n: int, A: list[int], B: list[int]) -> tuple[int, int, int]:
    sumB = [0, 0, 0]
    for j, b in enumerate(B, start=1):
        sumB[j % 3] += b
    area = [0, 0, 0]
    for i, a in enumerate(A, start=1):
        r = i % 3
        # 색 0,1,2
        area[0] += a * sumB[(0 - r) % 3]
        area[1] += a * sumB[(1 - r) % 3]
        area[2] += a * sumB[(2 - r) % 3]
    return area[0], area[1], area[2]

def main():
    # 입력
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 풀이
    c0, c1, c2 = solve(n, A, B)
    # 출력
    print(c0, c1, c2)

if __name__ == "__main__":
    main()
