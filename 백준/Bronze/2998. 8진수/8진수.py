import sys

input = sys.stdin.readline

def solve(binary_str: str) -> str:
    while len(binary_str) % 3 != 0:

        binary_str = '0' + binary_str

    result = []

    for i in range(0, len(binary_str), 3):

        group = binary_str[i:i+3]

        oct_digit = str(int(group, 2))  # 2진수 -> 정수 -> 문자열

        result.append(oct_digit)

    return ''.join(result)

def main():

    # 입력

    binary_str = input().strip()

    # 풀이

    result = solve(binary_str)

    # 출력

    print(result)

if __name__ == "__main__":

    main()