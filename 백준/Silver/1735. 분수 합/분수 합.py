def solve(a: int, b: int) -> int:
    
    while b != 0:
        [a, b] = [b, a%b]
    return a

def main():
    # 입력값
    a, A = map(int, input().split())
    b, B = map(int, input().split())
    # 풀이
    v = solve(a, A)
    A //= v
    a //= v
    v = solve(b, B)
    b //= v
    B //= v

    c = A*b + B*a # 분자
    C = A*B # 분모
    v = solve(c, C)

    
    # 출력
    print(c // v)
    print(C // v)


if __name__ == "__main__":
    main()