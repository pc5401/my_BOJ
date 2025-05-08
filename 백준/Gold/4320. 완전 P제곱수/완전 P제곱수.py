import sys
import math
input = sys.stdin.readline

def solve(x: int) -> int:
    if x == 1:
        return 1
    neg = x < 0
    a = abs(x)
            
    for p in range(31, 1, -1):
        if neg and p % 2 == 0:
            continue
        # approximate p-th root
        b = int(round(a ** (1.0 / p)))
        if b <= 0:
            continue
        # adjust around b
        for cand in (b-1, b, b+1):
            if cand > 0 and pow(cand, p) == a:
                return p
    return 1

def main():
    while True:
        line = input().strip()
        if not line:
            break
        x = int(line)
        if x == 0:
            break
        print(solve(x))

if __name__ == "__main__":
    main()
