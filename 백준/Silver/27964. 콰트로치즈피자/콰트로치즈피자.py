import sys
input = sys.stdin.readline


def solve(N: int, lst: list[str]) -> bool:
    cnt = 0

    for name in lst:
        if len(name) < 6:
            continue

        if name[-6:] == 'Cheese':
            cnt += 1

    return cnt >= 4


def main():
    # 입력값
    N = int(input())
    lst = list(set(input().rstrip().split()))
    
    # 풀이
    result = solve(N, lst)

    # 출력
    print('yummy' if result else 'sad')


if __name__ == "__main__":
    main()

