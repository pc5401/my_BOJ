import sys
input = sys.stdin.readline

def solve(N, K, forecast) -> int:
    L = N + K - 1
    arr = [0] * L
    for i, cast in enumerate(forecast):
        if cast == 'L':
            arr[i] = 1
    

    prefix_sum = [0] * (L + 1)
    for i in range(L):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
        
    max_rain = -1
    best_start = 0
    
    for start in range(N):
        cnt = prefix_sum[start + K] - prefix_sum[start]
        
        if cnt > max_rain:
            max_rain = cnt
            best_start = start

    return best_start + 1

def main():
    # 입력
    N, K = map(int, input().split())
    forecast = input().rstrip()

    # 풀이
    result = solve(N, K, forecast)

    # 출력
    print(result)

if __name__ == "__main__":
    main()