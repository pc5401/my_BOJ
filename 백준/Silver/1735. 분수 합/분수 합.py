def main():
    # 입력값
    a, A = map(int, input().split())
    b, B = map(int, input().split())
    # 풀이
    c = A*b + B*a # 분자
    C = A*B # 분모
    
    for num in range(min(c, C), 1, -1):
        if c % num == 0 and C % num == 0:
            c //= num
            C //= num
            break
    
    # 출력
    print(c)
    print(C)


if __name__ == "__main__":
    main()