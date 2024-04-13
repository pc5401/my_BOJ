import sys
input = sys.stdin.readline


def main():
    # 입력값
    A, B = input().split()
    A: str
    B: str

    a: int = int(A[::-1])
    b: int = int(B[::-1])
    print(max(a, b))


if __name__ == "__main__":
    main()