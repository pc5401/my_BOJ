import sys
input = sys.stdin.readline

def sieve(limit):
    p = [True] * (limit + 1)
    p[0] = p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if p[i]:
            step = i
            start = i * i
            p[start:limit+1:step] = [False] * (((limit - start) // step) + 1)
    return p

def try_match(first_idx, lock_v, adj, L, R):
    matchR = [-1] * R
    matchR[lock_v] = first_idx

    def dfs(u, seen):
        for v in adj[u]:
            if v == lock_v:
                continue
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or dfs(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False

    for u in range(L):
        if u == first_idx:
            continue
        seen = [False] * R
        if not dfs(u, seen):
            return False
    return True

def solve(nums):
    n = len(nums)
    primes = sieve(2000)

    first = nums[0]
    even = [x for x in nums if x % 2 == 0]
    odd  = [x for x in nums if x % 2 == 1]

    if len(even) != len(odd):
        return []

    if first % 2 == 0:
        left_vals = even
        right_vals = odd
    else:
        left_vals = odd
        right_vals = even

    L = len(left_vals)
    R = len(right_vals)

    idxL = {v:i for i, v in enumerate(left_vals)}
    idxR = {v:i for i, v in enumerate(right_vals)}

    adj = [[] for _ in range(L)]
    for i, a in enumerate(left_vals):
        for j, b in enumerate(right_vals):
            if primes[a + b]:
                adj[i].append(j)

    first_idx = idxL[first]
    cand_indices = []
    for j in adj[first_idx]:
        if try_match(first_idx, j, adj, L, R):
            cand_indices.append(j)

    return sorted(right_vals[j] for j in cand_indices)

def main():
    # 입력
    N = int(input().strip())
    nums = list(map(int, input().split()))

    # 풀이
    ans = solve(nums)

    # 출력
    if not ans:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main()
