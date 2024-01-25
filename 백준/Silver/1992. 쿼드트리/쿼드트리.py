import sys
input = sys.stdin.readline


def solve(r1, c1, r2, c2) -> str:
    if all(e == 1 for a in arr[r1:r2] for e in a[c1:c2]):
        return '1'
    elif all(e == 0 for a in arr[r1:r2] for e in a[c1:c2]):
        return '0'
    mid_r = (r1 + r2) // 2
    mid_c = (c1 + c2) // 2
    return '(' + solve(r1, c1, mid_r, mid_c) + solve(r1, mid_c, mid_r, c2) + solve(mid_r, c1, r2, mid_c) + solve(mid_r, mid_c, r2, c2) +')'


if __name__ == "__main__":
    # 입력값 처리
    N = int(input())
    arr = [list(map(int,list(input().rstrip()))) for _ in range(N)]
    print(solve(0, 0, N, N))
