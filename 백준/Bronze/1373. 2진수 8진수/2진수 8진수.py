import sys
input = sys.stdin.readline


def main():
    # 입력값
    bit = input().rstrip()
    bit: str
    # 풀이
    bit_to_int = int('0b'+bit, base=2)
    int_to_oct = oct(bit_to_int)
    # 출력
    print(int_to_oct[2:])

if __name__ == "__main__":
    main()