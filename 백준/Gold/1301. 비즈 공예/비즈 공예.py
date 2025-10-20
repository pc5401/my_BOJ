import sys
sys.setrecursionlimit(1 << 25)

def dfs(counts, last1, last2, N, memo):
    if counts in memo[last1+1][last2+1]:
        return memo[last1+1][last2+1][counts]
    if sum(counts) == 0:
        return 1
    total = 0
    for c in range(N):
        if counts[c] == 0:
            continue
        if c == last1 or c == last2:
            continue
        lst = list(counts)
        lst[c] -= 1
        nxt = tuple(lst)
        total += dfs(nxt, c, last1, N, memo)
    memo[last1+1][last2+1][counts] = total
    return total

def solve(N, cnts):
    memo = [[{} for _ in range(N+1)] for __ in range(N+1)]
    counts = tuple(cnts)
    return dfs(counts, -1, -1, N, memo)

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    # 입력
    N = int(next(it))
    cnts = [int(next(it)) for _ in range(N)]
    # 풀이
    ans = solve(N, cnts)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
