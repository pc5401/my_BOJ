import sys
input = sys.stdin.readline


def main():
    # 입력값
    N, A, B, C, D = map(int, input().split())
    # 풀이
    X = (N // A + 1) * B if N % A else (N // A) * B
    Y = (N // C + 1) * D if N % C else (N // C) * D
    # 출력
    print(min(X, Y))

if __name__ == "__main__":
    main()