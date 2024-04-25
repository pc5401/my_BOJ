import sys
input = sys.stdin.readline


def solve(N: int) -> int:
    count  = 1
    sum_of_consecutive = 1 # 1부터 연속된 자연수의 합
    i = 2

    while True:
        remaining = N - sum_of_consecutive 
        if remaining < i:
            break
        
        # remaining이 i로 나누어 떨어지면 연속된 i개의 합으로 N을 표현 가능
        if not remaining % i:
            count  += 1
        
        sum_of_consecutive  += i
        i += 1

    return count 


def main():
    # 입력값
    N: int = int(input())
    # 풀이
    result: int = solve(N)
    # 출력
    print(result)


if __name__ == "__main__":
    main()