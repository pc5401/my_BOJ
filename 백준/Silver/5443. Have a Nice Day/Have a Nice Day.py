import sys
from collections import Counter
input = sys.stdin.readline

def solve(D: int, M: int, Y: int) -> str:
    s = str(D) + str(M) + str(Y)
    freqs = Counter(s)
 
    if len(set(freqs.values())) != 1:
        return "no"
 
    parts = [D, M, Y // 100, Y % 100]
    total = sum(parts)
   
    if total % 2 != 0:
        return "no"
    half = total // 2
             
    for mask in range(1, 1 << 4):
        sm = 0
        for i in range(4):
            if mask & (1 << i):
                sm += parts[i]
        if sm == half:
            return "yes"
    return "no"

def main():
    # 입력
    t = int(input())
    # 풀이 & 출력
    for _ in range(t):
        D, M, Y = map(int, input().split())
        print(solve(D, M, Y))

if __name__ == "__main__":
    main()
