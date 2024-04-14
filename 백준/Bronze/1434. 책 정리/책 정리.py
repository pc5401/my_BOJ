import sys
input = sys.stdin.readline


def solve(N: int, M: int, A: list[int], B: list[int]) -> int:
    rtn = 0

    Q = A[::-1]
    box = Q.pop()
    for book in B:
        if box >= book:
            box = box - book
        else:
            rtn += box
            while Q:
                box = Q.pop()
                if box >= book :
                    box = box - book
                    break
                else:
                    rtn += box
    
    rtn += box
    while Q:
        rtn += Q.pop()
    return rtn


def main():
    N, M = map(int, input().split())
    N: int
    M: int

    A: list[int] = list(map(int, input().split()))
    B: list[int] = list(map(int, input().split()))

    result = solve(N, M, A, B)
    print(result)

if __name__ == "__main__":
    main()
