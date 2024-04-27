import sys
input = sys.stdin.readline


def is_prime(n: int) -> bool: # 밀러-라빈 소수 판별법
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n: # root n 까지만 확인하기
        if n % i == 0 or n % (i + 2) == 0: # 홀수만 확인하기
            return False
        i += 6 #  2와 3으로 나누어 떨어지지 않는 수만을 대상
   
    return True


def solve(n: int) -> int:
    if n < 3:
        return 2
    
    while True:
        if is_prime(n):
            return n

        n += 1


def main():
    # 입력값
    N: int = int(input())
    input_list: list[int] = [int(input()) for _ in range(N)]

    # 풀이
    result: list[int] = [solve(number) for number in input_list]

    # 출력
    for res in result:
        print(res)
    

if __name__ == "__main__":
    main()
