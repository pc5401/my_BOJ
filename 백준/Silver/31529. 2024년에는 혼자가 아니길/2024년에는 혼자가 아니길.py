import sys
input = sys.stdin.readline

def solve(X: int, Y: int) -> int:
    if Y < X or Y > 2*X:
        return -1
    
    val = 2024 * (2*X - Y)
    answer = val // 4  # 소수점 이하는 버림
    
    return answer
if __name__ == "__main__":
    # 입력값
    X, Y = map(int, input().split())
    
    # 풀이 
    result = solve(X, Y)
    
    # 출력
    print(result)
