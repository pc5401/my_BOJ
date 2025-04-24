import sys
input = sys.stdin.readline

def solve(N: int, M: int, P: int, ops: list[tuple[int,int]]) -> int:
    pos_hist = [0] * (M + 1)
    pos = 1
    pos_hist[0] = pos
    for i, (op, v) in enumerate(ops, start=1):
        if op == 1:
            pos = ((pos + v - 1) % N) + 1
        elif op == 2:
            pos = ((pos - 1 - (v % N)) % N) + 1
        else:  # op == 3
            pos = pos_hist[v]
        pos_hist[i] = pos
    return pos

def main():
    # 입력
    N, M = map(int, input().split())
    P = None  # P 불필요
    ops = [tuple(map(int, input().split())) for _ in range(M)]
    # 풀이
    result = solve(N, M, P, ops)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
