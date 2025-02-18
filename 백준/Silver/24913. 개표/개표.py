import sys
input = sys.stdin.readline


def solve(N: int, votes: list[int]) -> list[str]:
    others = [0] * N
    others_sum = 0
    others_max = 0
    me = 0
    result = []
    for typ, a, b in votes:
        if typ == 1:
            if b <= N:
                idx = b - 1
                others[idx] += a
                others_sum += a
                if others[idx] > others_max:
                    others_max = others[idx]
            else:
                me += a
        else:
            new_me = me + a
            y = b
            m = others_max
            required = N * m - others_sum
            if y <= required:
                new_max = m
            else:
                remainder = y - required
                inc = (remainder + N - 1) // N
                new_max = m + inc
            result.append("YES" if new_me > new_max else "NO")
    return result

def main():
    # 입력값
    N, Q = map(int, input().split())
    N: int
    Q: int
    votes: list[int] = [list(map(int, input().split())) for _ in range(Q)]

    # 풀이
    result: list[str] = solve(N, votes)

    # 출력
    for res in result:
        print(res)
    
if __name__ == "__main__":
    main()

