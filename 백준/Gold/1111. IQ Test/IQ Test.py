import sys
input = sys.stdin.readline

is_same_result = lambda numbers: all(x == numbers[0] for x in numbers)

def is_B(n: int, a: int, b: int, numbers: list[int]) -> bool:
    return any(numbers[i] != a * numbers[i-1] + b for i in range(1, n))

def get_a_b(x0, x1, x2):
    # ZeroDivisionError 방지
    if x0 == x1:
        return None
    a = (x1 - x2) // (x0 - x1)  # 정수 나눗셈
    b = x1 - (x0 * a)
    return (a, b)

def solve(n: int, numbers: list[int]) -> int:
    if n == 1:
        return 'A'
    elif n == 2 and numbers[0] != numbers[1]:
        return 'A'
    elif is_same_result(numbers):
        return numbers[0]

    a_b = get_a_b(numbers[0], numbers[1], numbers[2])
    if a_b is None:  # ZeroDivisionError가 발생할 경우
        return 'B'
    
    a, b = a_b
    if is_B(n, a, b, numbers):
        return 'B'
    
    return a * numbers[-1] + b

def main():
    # 입력값
    N = int(input())
    numbers = list(map(int, input().split()))
    # 풀이
    result = solve(N, numbers)

    # 출력
    print(result)

if __name__ == "__main__":
    main()

