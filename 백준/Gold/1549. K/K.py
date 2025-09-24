import sys
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.t = [0]*(n+1)
    def add(self, i, v):
        while i <= self.n:
            self.t[i] += v
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s
    def find_kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length())
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.t[nxt] < k:
                k -= self.t[nxt]
                idx = nxt
            bit >>= 1
        return idx + 1

def solve(n, A):
    pref = [0]*(n+1)
    for i in range(n):
        pref[i+1] = pref[i] + A[i]

    best_k = 0
    best_diff = 10**30

    for k in range(1, n//2 + 1):
        m = n - k + 1
        S = [pref[i+k] - pref[i] for i in range(m)]
        vals = sorted(set(S))
        pos = {v: i+1 for i, v in enumerate(vals)}
        bit = BIT(len(vals))

        cur = 10**30
        total = 0
        for j in range(m):
            if j - k >= 0:
                bit.add(pos[S[j-k]], 1)
                total += 1
            if j >= k and total:
                idx = pos[S[j]]
                le = bit.sum(idx)
                if le:
                    pidx = bit.find_kth(le)
                    pv = vals[pidx-1]
                    d = S[j] - pv
                    if d < cur:
                        cur = d
                lt = bit.sum(idx-1)
                if total > lt:
                    sidx = bit.find_kth(lt+1)
                    sv = vals[sidx-1]
                    d2 = sv - S[j]
                    if d2 < cur:
                        cur = d2

        if cur < best_diff or (cur == best_diff and k > best_k):
            best_diff = cur
            best_k = k

    return best_k, best_diff

def main():
    # 입력
    n = int(input().strip())
    A = list(map(int, input().split()))

    # 풀이
    k, diff = solve(n, A)

    # 출력
    print(k)
    print(diff)

if __name__ == "__main__":
    main()
