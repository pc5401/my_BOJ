import sys
input = sys.stdin.readline

def solve(N: int, A: list[int]) -> int:
    gmin, gmax = min(A), max(A)
    
    if gmin == gmax:
        return 1

    ans = N
    last_min = -1
    last_max = -1

    for i in range(N):
        # 최솟갑이면, 확인
        if A[i] == gmin:
            last_min = i
            if last_max != -1:
                ans = min(ans, i - last_max + 1)
        
        # 최대값이면 확인
        if A[i] == gmax:
            last_max = i
            if last_min != -1:
                ans = min(ans, i - last_min + 1)
                
    return ans

def main():
    # 입력
    N = int(input())
    A = list(map(int, input().split()))
    
    # 풀이
    result = solve(N, A)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
