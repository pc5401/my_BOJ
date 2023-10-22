if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    
    if N % 2 == 0:
        a, b = N//2 + 1, N // 2 + 1
    else:
        a, b = N//2 + 2  , N // 2 + 1

    print(a*b)