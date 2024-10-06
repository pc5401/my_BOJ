import sys
input = sys.stdin.readline

def get_sum_arr(N: int, A: list[int]) -> list[int]:
    rtn = [0] * (N+1)
    for i in range(N):
        rtn[i+1] = A[i] + rtn[i]
    
    return rtn

def solve(B: list[list[int]], sum_arr: list[int]) -> list[int]:
    rtn = []
    
    for x, y in B:
        rtn.append(sum_arr[y] - sum_arr[x-1])

    return rtn

if __name__ == "__main__":
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = [map(int, input().split()) for _ in range(M)]

    # 풀이
    sum_arr = get_sum_arr(N, A)
    result = solve(B, sum_arr)

    # 출력
    for res in result:
        print(res)