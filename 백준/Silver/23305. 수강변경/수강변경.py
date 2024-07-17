import sys
input = sys.stdin.readline


def solve(N: int, A: list, B: list) -> int:
    a = sorted(A)
    b = sorted(B)
    cnt = 0
    i, j = 0, 0
    while j < N and i < N:
        if a[i] == b[j]:
            i += 1
            j += 1
            cnt += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    
    return N - cnt

def main():
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 풀이
    result: list[int] = solve(N, A, B)
    # 출력
    print(result)


if __name__ == "__main__":
    main()

