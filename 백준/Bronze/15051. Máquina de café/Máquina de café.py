import sys
input = sys.stdin.readline


def main():
    # 입력값
    A = [int(input()) for _ in range(3)]
    # 풀이
    result = []
    for i in range(3):
        sumA = 0
        for j in range(3):
            sumA += (abs(i-j) * 2 * A[j])
        result.append(sumA)
    # 출력
    print(min(result))

if __name__ == "__main__":
    main()