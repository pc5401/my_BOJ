if __name__ == '__main__':
    N = int(input())
    lst = list(map(int,input().split()))
    # LIS 는 푸는 방식은 2 가지다. DP 그리고 이분탐색
    # DP 로 접근하자. 초기값은 최소 길이 '1' 이다.
    dp = [1] * N
    for i in range(1,N): # 첫 번째는 결국 1 이므로 두 번째 인덱스(0) 부터 시작
        for j in range(0,i): # 이제 까지 온 (i) 기준으로 최장 길이 계산
            if lst[i] > lst[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1 # j 기준으로 최댓값 보다 +1 
    # 최댓값 출력
    print(max(dp))