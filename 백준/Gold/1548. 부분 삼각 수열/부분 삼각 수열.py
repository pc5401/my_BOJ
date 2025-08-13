import sys
input = sys.stdin.readline

def solve(N, A):
    A.sort()
    if N <= 2:
        return N
    ans = 2
    l = 0
    for r in range(2, N):
        while l < r - 1 and A[l] + A[l + 1] <= A[r]:
            l += 1
        if A[l] + A[l + 1] > A[r]:
            length = r - l + 1
            if length > ans:
                ans = length
    return ans

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
