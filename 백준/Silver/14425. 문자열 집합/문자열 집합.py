import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력값
    N, M = map(int, input().split())
    S = {input().rstrip() for _ in range(N)}
    lst = [input().rstrip() for _ in range(M)]
    
    # 풀이 
    result = [ 1 if v in S else 0 for v in lst]
    
    # 출력
    
    print(sum(result))