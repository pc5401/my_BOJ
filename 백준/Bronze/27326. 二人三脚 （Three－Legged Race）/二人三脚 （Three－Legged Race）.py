import sys
input = sys.stdin.readline

def solve(n: int, groups: list[int]) -> int:
    ans = 0
    for g in groups:
        ans ^= g
    return ans

def main():
    # 입력
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    # 풀이
    ans = solve(n, arr)
    
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
