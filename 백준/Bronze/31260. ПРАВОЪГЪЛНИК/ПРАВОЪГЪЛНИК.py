import sys
input = sys.stdin.readline

def solve(x: int, y: int, d: int):
    P = x * 100 + y
    s = P // 2
    A = (s + d) // 2
    B = (s - d) // 2
    return ((A // 100, A % 100), (B // 100, B % 100))

def main():
    # 입력
    x, y = map(int, input().split())
    d = int(input())
    
    # 풀이
    res_A, res_B = solve(x, y, d)

    
    # 출력
    print(*res_A)
    print(*res_B)

if __name__ == "__main__":
    main()
