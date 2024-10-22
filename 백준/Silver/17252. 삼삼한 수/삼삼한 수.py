import sys
import itertools
input = sys.stdin.readline      


def solve(N: int) -> bool:
    lst = [3**i for i in range(20) if 3**i <= N]
    for i in range(1, len(lst)+1):
        for values in itertools.combinations(lst, i):
            if N == sum(values):
                return True

    return False


if __name__ == "__main__":
    # 입력값
    N = int(input())

    # 풀이
    result = solve(N)

    # 출력    
    print('YES' if result else 'NO')

