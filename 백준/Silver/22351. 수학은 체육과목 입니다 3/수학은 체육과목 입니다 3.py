import sys
input = sys.stdin.readline

def getNumber(n: int, L: int) -> str:
    rtn = str(n)

    while len(rtn) < L:
        n += 1
        rtn += str(n)
    
    return (rtn, str(n))


def solve(N: int) -> tuple:
    L = len(N)

    for i in range(1, L):
        fst = int(N[:i])
        M, last = getNumber(fst, L)
        if M == N:
            return (fst, last)

    return (N, N)




def main():
    # 입력값
    N = input().rstrip()
    
    # 풀이
    result = solve(N)

    # 출력
    print(*result)


if __name__ == "__main__":
    main()


