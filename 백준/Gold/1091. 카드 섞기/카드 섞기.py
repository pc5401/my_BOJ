import sys
input = sys.stdin.readline

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def crt_merge(a1, m1, a2, m2):
    g, p, q = extgcd(m1, m2)
    diff = a2 - a1
    if diff % g != 0:
        return None
    lcm = m1 // g * m2
    x = (diff // g * p) % (m2 // g)
    t = (a1 + m1 * x) % lcm
    return t, lcm

def find_shift(R, Pseq):
    L = len(R)
    for t in range(L):
        ok = True
        for k in range(L):
            if R[(k + t) % L] != Pseq[k]:
                ok = False
                break
        if ok:
            return t
    return -1

def minimal_period(seq):
    L = len(seq)
    for d in range(1, L + 1):
        if L % d != 0:
            continue
        ok = True
        for i in range(L):
            if seq[i] != seq[(i + d) % L]:
                ok = False
                break
        if ok:
            return d
    return L

def solve(N, P, S):
    visited = [False] * N
    congr = []  # list of (t ≡ a mod m)
    for i in range(N):
        if visited[i]:
            continue
        cyc = []
        x = i
        while not visited[x]:
            visited[x] = True
            cyc.append(x)
            x = S[x]

        Rseq = [idx % 3 for idx in cyc]
        Pseq = [P[idx] for idx in cyc]

        t0 = find_shift(Rseq, Pseq)
        if t0 == -1:
            return -1

        d = minimal_period(Rseq)
        t0 %= d
        if d != 1:
            congr.append((t0, d))

    if not congr:
        return 0

    a, m = congr[0]
    for a2, m2 in congr[1:]:
        merged = crt_merge(a, m, a2, m2)
        if merged is None:
            return -1
        a, m = merged
    return a

def main():
    # 입력
    N = int(input().strip())
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))
    # 풀이
    ans = solve(N, P, S)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()

