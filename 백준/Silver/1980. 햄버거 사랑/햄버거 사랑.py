import sys
input = sys.stdin.readline


def solve(N: int, M: int, T: int) -> list[int]:
    n, m = min(N, M), max(N, M)
    k = T // m
    rtn = [0, 1e9]

    for i in range(k, -1, -1):
        cnt = i
        cnt += (T - i * m) // n
        time = (T - i * m) % n

        if rtn[1] > time:
            rtn[0] = cnt
            rtn[1] = time
        
        elif rtn[1] == time and rtn[0] < cnt:
            rtn[0] = cnt

    return rtn




def main():
    # 입력값
    N, M, T = map(int, input().split())
    # 풀이
    result: list[int] = solve(N, M, T)

    # 출력
    print(*result)
    

if __name__ == "__main__":
    main()
