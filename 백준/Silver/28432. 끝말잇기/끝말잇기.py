import sys
input = sys.stdin.readline

def solve(N: int, S: list[str], A: list[str]) -> list[str]:
    rtn = []
    check_list = set(S)

    if N == 1:
        return A[0]

    if S[0] == '?':
        start = ''
        end = S[1][0]
    elif S[-1] == '?':
        start = S[-2][-1]
        end = ''
    else:
        for i in range(1, N-1):
            if S[i] == '?':
                start = S[i-1][-1]
                end = S[i+1][0]

    for a in A:
        if not start and a[-1] == end and not a in check_list:
            return a
        elif not end and a[0] == start and not a in check_list:
            return a
        elif start == a[0] and end == a[-1] and not a in check_list:
            return a

    return A[0]

if __name__ == "__main__":
    # 입력값
    N = int(input())
    S = [input().rstrip() for _ in range(N)]
    M = int(input())
    A = [input().rstrip() for _ in range(M)]

    # 풀이
    result = solve(N, S, A)

    # 출력
    print(result)
