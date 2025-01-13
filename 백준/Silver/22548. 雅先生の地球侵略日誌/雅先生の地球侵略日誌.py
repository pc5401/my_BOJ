import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    k = 0
    power = 1

    while power < N:
        power *= 3
        k += 1

    return k


if __name__ == '__main__':
    # 입력값
    N = int(input())
    
    # 풀이
    result = solve(N)

    # 출력
    print(result)
