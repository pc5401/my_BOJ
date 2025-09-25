import sys
input = sys.stdin.readline

def solve(N, M, ops):
    trains = [0] * (N + 1)
    mask = (1 << 20) - 1

    for op in ops:
        t = op[0]
        if t == 1:
            _, i, x = op
            trains[i] |= (1 << (x - 1))
        elif t == 2:
            _, i, x = op
            trains[i] &= ~(1 << (x - 1))
        elif t == 3:
            _, i = op
            trains[i] = (trains[i] << 1) & mask
        else:
            _, i = op
            trains[i] >>= 1

    return len(set(trains[1:]))

def main():
    # 입력
    N, M = map(int, input().split())
    ops = []
    for _ in range(M):
        parts = input().split()
        t = int(parts[0])
        if t in (1, 2):
            ops.append((t, int(parts[1]), int(parts[2])))
        else:
            ops.append((t, int(parts[1])))

    # 풀이
    result = solve(N, M, ops)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
