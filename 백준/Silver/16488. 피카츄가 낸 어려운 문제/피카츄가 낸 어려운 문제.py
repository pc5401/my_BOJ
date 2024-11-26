import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력값
    N, K = map(int, input().split())
    # 풀이
    result = (lambda x, y : x*x*y)(N, K)
    
    # 출력
    print(result)