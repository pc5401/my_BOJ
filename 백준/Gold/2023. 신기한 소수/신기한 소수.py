import sys
import math
input = sys.stdin.readline

# 초기 소수 리스트
prime_numbers = [2, 3, 5, 7]

# 소수 판별 함수
def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    sqrt_n = int(math.isqrt(number)) + 1
    for i in range(3, sqrt_n, 2):
        if number % i == 0:
            return False
    return True

def get_prime_nums(num: int, level: int, end: int) -> list[int]:
    if level == end:
        return [num]
    
    rtn = []
    ahead = num * 10

    for i in range(1, 10, 2):
        if i == 5:
            continue
        value = ahead + i
        if is_prime(value):
            rtn.extend(get_prime_nums(value, level + 1, end))
            
    return rtn

def solve(N: int) -> list[int]:
    rtn = []

    for number in prime_numbers:
        rtn.extend(get_prime_nums(number, 1, N))
        
    return rtn

if __name__ == "__main__":
    # 입력값
    N = int(input())

    # 풀이
    if N == 1:
        result = prime_numbers
    else:      
        result = solve(N)

    # 출력    
    for res in sorted(result):
        print(res)
