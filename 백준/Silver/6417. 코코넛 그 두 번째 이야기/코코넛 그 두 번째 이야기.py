import sys
input = sys.stdin.read

def solve(N: int) -> str:
    max_K = 0
    # K는 2부터 시작하여 N까지 탐색
    # 하지만 효율성을 위해 K의 최대 값을 10,000으로 제한
    for K in range(2, min(N, 10000) + 1):
        C = N
        success = True
        for _ in range(K):
            if (C - 1) % K != 0:
                success = False
                break
            C = (C - 1) * (K - 1) // K
        if success and C % K == 0:
            if K > max_K:
                max_K = K
    if max_K > 0:
        return f"{N} coconuts, {max_K} people and 1 monkey"
    else:
        return f"{N} coconuts, no solution"
    
def main():
    # 입력값
    data = list(map(int, input().split()))
    
    # 결과 저장 리스트
    result = []
    
    for N in data:
        if N == -1:
            break
        result.append(solve(N))
    
    # 결과 출력
    for res in result:
        print(res)

if __name__ == '__main__':
    main()