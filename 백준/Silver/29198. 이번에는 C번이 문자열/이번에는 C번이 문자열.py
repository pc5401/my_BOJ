import sys
input = sys.stdin.readline

def solve(n: int, m: int, k: int, strs: list[str]) -> str:
    dp = [None] * (k + 1)
    dp[0] = (0,) * 26
    for s in strs:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('A')] += 1
        freq = tuple(freq)
        for j in range(k-1, -1, -1):
            if dp[j] is None: continue
            cand = tuple(dp[j][i] + freq[i] for i in range(26))
            if dp[j+1] is None or cand > dp[j+1]:
                dp[j+1] = cand
    ans_vec = dp[k]
    res = []
    for i in range(26):
        res.append(chr(ord('A') + i) * ans_vec[i])
    return "".join(res)

def main():
    # 입력
    n, m, k = map(int, input().split())
    strs = [input().strip() for _ in range(n)]
    
    # 풀이
    ans = solve(n, m, k, strs)
    
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
