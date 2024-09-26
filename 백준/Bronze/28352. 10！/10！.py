def main():
    # 입력값
    N = int(input())
    
    # N! 계산
    result = 1
    for i in range(2, N+1):
        result *= i

    # 1주의 초: 7 * 24 * 60 * 60 = 604800
    one_week_seconds = 7 * 24 * 60 * 60
    
    # N! 초가 몇 주에 해당하는지 계산
    weeks = result // one_week_seconds

    # 결과 출력
    print(weeks)

if __name__ == "__main__":
    main()
