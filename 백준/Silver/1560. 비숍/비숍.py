import sys
input = sys.stdin.readline

def solve(n) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * n - 2

def main():
    # 입력
    N = int(input())
    
    # 풀이
    result = solve(N)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
