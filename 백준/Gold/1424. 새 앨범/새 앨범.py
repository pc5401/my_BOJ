import sys
input = sys.stdin.readline

def solve(N, L, C):
    Kmax = (C + 1) // (L + 1)
    Kbest = Kmax if Kmax % 13 != 0 else Kmax - 1

    d, r = divmod(N, Kbest)

    if r == 0:
        return d

    if d == 0:
        return 2 if r % 13 == 0 else 1

    if r % 13 != 0:
        return d + 1

    if Kbest % 13 == 1 and r == Kbest - 1:
        return d + 2

    return d + 1

def main():
    # 입력
    N = int(input().strip())
    L = int(input().strip())
    C = int(input().strip())

    # 풀이
    result = solve(N, L, C)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
