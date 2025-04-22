import sys
from collections import Counter
input = sys.stdin.readline

def solve(S: str) -> str:
    n = len(S)
    cnt = Counter(S)
    result = [None] * n

    def feasible():
        free_pos = [i for i, v in enumerate(result) if v is None]

        allowed = Counter()
        for i in free_pos:
            j = n - 1 - i
            for c in cnt:
                if cnt[c] == 0: 
                    continue
                
                if result[j] == c:
                    continue
                allowed[c] += 1

        for c in cnt:
            if cnt[c] > allowed[c]:
                return False
        return True

    for i in range(n):
        j = n - 1 - i
        for c in sorted(cnt):
            if cnt[c] == 0:
                continue
            
            if result[j] == c:
                continue
            
            result[i] = c
            cnt[c] -= 1
            if feasible():
                break  # keep c
            
            cnt[c] += 1
            result[i] = None
        else:
            return "-1"

    for i in range((n)//2):
        if result[i] == result[n-1-i]:
            return "-1"
    return "".join(result)

def main():
    S = input().strip()
    print(solve(S))

if __name__ == "__main__":
    main()
