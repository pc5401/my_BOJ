import sys
input = sys.stdin.readline


def solve(N: int, votes: list[int]) -> list[bool]:
    table = [0] * N
    rtn = []
    other = 0
    me = 0

    for n, a, b in votes:
        if n == 1 and b-1 < N:
            table[b-1] += a
            if table[b-1] > other:
                other = table[b-1]
        
        elif n == 1:
            me += a

        elif n == 2:
            rtn.append(me + a > other + (b/N) )

    return rtn

def main():
    # 입력값
    N, Q = map(int, input().split())
    N: int
    Q: int
    votes: list[int] = [list(map(int, input().split())) for _ in range(Q)]

    # 풀이
    result = solve(N, votes)

    # 출력
    for res in result:
        print('YES' if res else 'NO')
    
if __name__ == "__main__":
    main()

