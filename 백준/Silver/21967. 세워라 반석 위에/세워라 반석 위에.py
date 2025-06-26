import sys
input = sys.stdin.readline

def solve(N: int, A: list[int]) -> int:
    counts = [0] * 11 
    l = 0
    best = 0
    for r in range(N):
        counts[A[r]] += 1

        while 1:
            mn = 1
            while mn <= 10 and counts[mn] == 0:
                mn += 1
            mx = 10
            while mx >= 1 and counts[mx] == 0:
                mx -= 1
            if mx - mn <= 2:
                break
            counts[A[l]] -= 1
            l += 1

        length = r - l + 1
        if length > best:
            best = length
    return best

def main():
    # 입력
    N = int(input().strip())
    A = list(map(int, input().split()))
    # 풀이
    result = solve(N, A)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
