import sys
import math
input = sys.stdin.readline


def main():
    # 입력값
    input_data = []
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        input_data.append((n, k))

    # # 풀이
    result = [math.comb(n, k) for n, k in input_data]

    # # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
