import sys, math
input = sys.stdin.readline

def solve(x: int, y: int) -> int:
    low, high, ans = 0, 10000, 0
    while low <= high:
        mid = (low + high) // 2
        R = mid
        req = 50 * R - x
        if req <= 0:
            L = 0
        else:
            L = math.ceil(req / 3)
        U = min(y // 2, 16 * R)
        if L <= U:
            ans = R
            low = mid + 1
        else:
            high = mid - 1
    return ans

def main():
    # 입력
    x, y = map(int, input().split())
    
    # 풀이
    result = solve(x, y)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
