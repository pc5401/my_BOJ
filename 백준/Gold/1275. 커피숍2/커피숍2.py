import sys

def add(bit, n, i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i

def sum_prefix(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

def range_sum(bit, l, r):
    if l > r:
        l, r = r, l
    return sum_prefix(bit, r) - sum_prefix(bit, l - 1)

def solve(n, q, arr, ops):
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        add(bit, n, i, arr[i])
    out = []
    for x, y, a, b in ops:
        out.append(str(range_sum(bit, x, y)))
        delta = b - arr[a]
        arr[a] = b
        add(bit, n, a, delta)
    return out

def main():
    #입력
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    ops = [tuple(map(int, input().split())) for _ in range(Q)]
    #풀이
    ans = solve(N, Q, A, ops)
    #출력
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
