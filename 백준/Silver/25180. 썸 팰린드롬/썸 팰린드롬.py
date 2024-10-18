import sys
input = sys.stdin.readline      


def solve(N: int) -> int:
    if N < 10:
        return 1
    div, mod = divmod(N, 18)
    
    if mod == 0:
        return div * 2
    elif mod <= 9:
        return div * 2 + 1
    elif mod <= 18 and mod % 2 == 0:
        return div * 2 + 2
    else:
        return div * 2 + 3


if __name__ == "__main__":
    # 입력값
    N = int(input())
    
    # 풀이
    result = solve(N)

    # 출력
    print(result)