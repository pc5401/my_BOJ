import sys
input = sys.stdin.readline

def solve(N: int, lst: int) -> int:
    diff = sum(lst[0] - lst[i] for i in range(len(lst)))
    left = 0

    for i, v in enumerate(lst):
        if left >= diff:
            return i
        diff -= (v - lst[i+1]) * (N-i-1)
        left += v

    return i
        

if __name__ == "__main__":
    # 입력값
    N = int(input())
    lst = list(map(int, input().split()))
    
    # 풀이
    result = solve(N, sorted(lst, reverse=True))
    
    # 출력    
    print(result)