import sys
input = sys.stdin.readline


def solve(k: int, lst: list[int]) -> str:
    N, socres = lst[0], lst[1:]
    gap = 0
    socres.sort()

    for i in range(N-1):
        if socres[i+1] - socres[i] > gap:
            gap = socres[i+1] - socres[i]
    
    return f'Class {k}\nMax {socres[N-1]}, Min {socres[0]}, Largest gap {gap}'


def main():
    # 입력값
    K = int(input())
    result = [solve(k, list(map(int, input().split()))) for k in range(1, K+1)]

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()