import sys
import math
input = sys.stdin.readline

def solve(S: int, P: int) -> int:
    if P == 0:
        return 2
    if P == S:
        return 1

    lnP = math.log(P)
    lnS = math.log(S)
    eps = 1e-12
    for k in range(2, 101):
        if k * (lnS - math.log(k)) + eps >= lnP:
            return k
    return -1

def main():
    # 입력
    S, P = map(int, input().split())
    # 풀이
    result = solve(S, P)
    # 출력
    print(result)

if __name__ == "__main__":
    main()

