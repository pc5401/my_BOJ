import sys
input = sys.stdin.readline


def solve(pika: str) -> int:
    N = len(pika)
    i = 0
    while N > i:
        w = pika[i]

        if w == 'p' and i+1 < N and pika[i+1] == 'i':
                i += 2
                continue
        elif w == 'k' and i+1 < N and pika[i+1] == 'a':
                i += 2
                continue
        elif w == 'c' and i+2 < N and pika[i+1] == 'h' and pika[i+2] == 'u':
                i += 3
                continue
        else:
            return False
    
    return True


def main():
    # 입력값
    pika: str = input().rstrip()

    # 풀이
    result: bool = solve(pika)

    # 출력
    print('YES' if result else 'NO')


if __name__ == "__main__":
    main()
