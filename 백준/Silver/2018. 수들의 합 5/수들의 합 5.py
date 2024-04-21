import sys
input = sys.stdin.readline


def solve(N: int) -> int:
    rtn = 1
    facto_value = 1
    i = 2

    while True:
        number = N - facto_value
        if number < i:
            break
        
        if not number % i:
            rtn += 1
        
        facto_value += i
        i += 1

    return rtn



def main():
    # 입력값
    N: int = int(input())
    # 풀이
    result: int = solve(N)
    # 출력
    print(result)


if __name__ == "__main__":
    main()