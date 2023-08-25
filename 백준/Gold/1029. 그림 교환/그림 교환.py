import sys
input = sys.stdin.readline


def solve(n: int, lst: list):
    maxV = 1
    dp = [[[0 for price in range(10)] # 가격 0~9
            for visit in range(1 << n)] # 방문 경우
                for i in range(n)] # 예술가 수
    dp[0][1][0] = 1

    for visit in range(1 << n): # 모든 방문을 확인
        for i in range(n): # 예술가 확인
            for price in range(10): # 가격 확인
                if not dp[i][visit][price]: # 초기화된 값이 시작점 -> 이후 확장 
                    continue

                for j in range(n): # 다음 예술가 전부 확인
                    bit_value = (1 << j)
                    next_price = lst[i][j]
                    next_visit = visit | bit_value
                    
                    if price > next_price: # 1번 조건 : 가격 확인
                        continue
                    if visit & bit_value: # 2번 조건 :  중복 확인
                        continue
                    
                    # dp 테이블 업그레이드
                    v = dp[i][visit][price] + 1 # 방문 증가 저장
                    dp[j][next_visit][next_price] = max(v, dp[j][next_visit][next_price])
                    maxV = max(maxV, v)
    
    return maxV

if __name__ == '__main__':
    N = int(input())
    Arr = [list(map(int,input().rstrip())) for _ in range(N)]
    print(solve(N, Arr))
