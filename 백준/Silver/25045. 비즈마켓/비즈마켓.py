import sys
input = sys.stdin.readline

def solve(N: int, M: int, A: list[int], B: list[int]) -> int:
    A.sort(reverse=True)
    B.sort()
    result = 0
    j = 0
    for a in A:
        if j < M and B[j] <= a:
            result += a - B[j]
            j += 1
    return result

def main():
    # 입력
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 풀이
    result = solve(N, M, A, B)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
