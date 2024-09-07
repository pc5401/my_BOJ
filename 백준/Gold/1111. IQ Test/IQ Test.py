import sys
input = sys.stdin.readline

def is_result(n: int, a: int, b: int, numbers: list[int]) -> bool:
    for i in range(1, n):
        if numbers[i] != a * numbers[i-1] + b:
            return False
    
    return True


def get_last_number(n, a, b):
    return a*n + b


def solve(n: int, numbers: list[int]) -> int:
    last_numbers = set()
    for i in range(201):
        for j in range(20001):
            for d in [(1,1), (-1, 1),(1, -1),(-1, -1)]:
                a = i*d[0]
                b = j*d[1]
                if is_result(n, a, b, numbers):
                    last_numbers.add(get_last_number(numbers[-1], a, b))
                    if len(last_numbers) > 1:
                        return 'A'

    return last_numbers.pop() if last_numbers else 'B'

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