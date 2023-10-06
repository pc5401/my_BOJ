import sys
import collections
input = sys.stdin.readline

def stack_box(L: int, W: int, H: int, A: float) -> int:
    l = L // A
    w = W // A
    h = H // A
    return l * w * h

def solve(N: int, L: int, W: int, H: int) -> int:
    lo = 0
    hi = max(L, W, H) + 1
    
    for _ in range(10000):
        A = (lo+hi) / 2
        cnt = stack_box(L, W, H, A)
        if cnt >= N:
            lo = A
        else:
            hi = A
    
    return lo


if __name__ == "__main__":
    # 입력 & 전처리
    N, L, W, H = map(int, input().split())
    print(solve(N, L, W, H))
    