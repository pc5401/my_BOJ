import sys
input = sys.stdin.readline

def get_result(p: int, lo: int, hi: int, lst) -> int:
    while lo <= hi:
        mid = (lo + hi) // 2

        if lst[mid] > p:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return lo

def solve(N: int, Q: int, K: list[int], P: list[int]) -> list[int]:
    lst = [0] * (N + 1)
    for i in range(N):
        lst[i + 1] = K[i] + lst[i]

    result = []
    for p in P:
        day = get_result(p, 0, N, lst)
        if day > N:
            result.append(-1)
        else:
            result.append(day)
    
    return result

if __name__ == "__main__":
    # 입력값
    N, Q = map(int, input().split())
    K = list(map(int, input().split()))
    P = list(map(int, input().split()))

    # 풀이
    result = solve(N, Q, K, P)

    # 출력
    for res in result:
        print(res)
