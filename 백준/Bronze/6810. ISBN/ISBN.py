import sys
input = sys.stdin.readline


def solve(last_three : list[int]) -> int:
    fixed_part = [9,7,8,0,9,2,1,4,1,8]
    isbn = fixed_part + last_three

    one_three_sum = 0
    for i, digit in enumerate(isbn):

        if i % 2 == 0:
            one_three_sum += digit * 1
        else:
            one_three_sum += digit * 3

    return one_three_sum


def main():
    # 입력값
    last_three : list[int] = [int(input()) for _ in range(3)]
    # 풀이
    result: list[int] = solve(last_three)

    # 출력
    print(f"The 1-3-sum is {result}")
    

if __name__ == "__main__":
    main()
