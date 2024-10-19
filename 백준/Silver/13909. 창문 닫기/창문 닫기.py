import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    result = 0
    num = 1

    while num*num <= N:
        result += 1
        num += 1
    
    return result

if __name__ == "__main__":
    # 입력값
    N = int(input())
    
    # 풀이
    result = solve(N)

    # 출력
    print(result)