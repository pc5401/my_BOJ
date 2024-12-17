import sys
input = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def solve(N: int, S: int, A: list[int]) -> int:
    rtn = abs(S - A[0])

    for i in range(1, N):
        dist = abs(S - A[i])
        rtn = gcd(rtn, dist)

        if rtn == 1:
            break
    
    return rtn
    

if __name__ == "__main__":
    N, S  = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 풀이
    result = solve(N, S, A)
    
    # 출력
    print(result)
