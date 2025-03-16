import sys
input = sys.stdin.readline

def solve(N: int, A: int, B: int, C: int, tops: list[int]) -> int:
    tops.sort(reverse=True)
    total_cal = C
    total_cost = A
    best = total_cal // total_cost
    for t in tops:
        total_cal += t
        total_cost += B
        best = max(best, total_cal // total_cost)
    return best

def main():
    # 입력
    N = int(input().strip())
    A, B = map(int, input().split())
    C = int(input().strip())
    tops = [int(input().strip()) for _ in range(N)]
    
    # 풀이
    ans = solve(N, A, B, C, tops)
    
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
