import sys
input = sys.stdin.readline

def solve(n: int, T: int, r: list[int]) -> list[int]:
    ans = []
    if n == 1:
        return [1] * T
    for _ in range(T):
        max_val = -1
        max_idx = -1
        for i in range(n):
            if r[i] > max_val or (r[i] == max_val and i < max_idx):
                max_val = r[i]
                max_idx = i
        ans.append(max_idx + 1)
        v = r[max_idx]
        r[max_idx] = 0
        d = v // (n - 1)
        rem = v % (n - 1)
        for i in range(n):
            if i == max_idx:
                continue
            r[i] += d
        for i in range(n):
            if i == max_idx:
                continue
            if rem:
                r[i] += 1
                rem -= 1
            else:
                break
    return ans

def main():
    # 입력
    n, T = map(int, input().split())
    r = [int(input().strip()) for _ in range(n)]
    
    # 풀이
    ans = solve(n, T, r)
    
    # 출력
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
