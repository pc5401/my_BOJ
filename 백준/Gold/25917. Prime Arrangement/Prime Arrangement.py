import sys
input = sys.stdin.readline

MOD = 998_244_353

def solve(R, C):
    # 총 원소 수
    n = R * C
    
    # (R * C)! 계산
    fact_n = 1
    for i in range(1, n+1):
        fact_n = (fact_n * i) % MOD
        
    # R! 계산
    fact_R = 1
    for i in range(1, R+1):
        fact_R = (fact_R * i) % MOD
        
    # 모듈러 역원
    inv_fact_R = pow(fact_R, MOD-2, MOD)
    
    return (fact_n * inv_fact_R) % MOD

def main():
    # 입력
    R, C = map(int, input().split())
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    
    # 풀이
    result = solve(R, C)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()