import sys
import bisect
input = sys.stdin.readline

def count_upto(X: int, p1: int, p2: int, p3: int) -> int:
    # p1, p2, p3 거듭제곱들 계산
    p1_pows = []
    v = 1
    while v <= X:
        p1_pows.append(v)
        v *= p1
    p2_pows = []
    v = 1
    while v <= X:
        p2_pows.append(v)
        v *= p2
    p3_pows = []
    v = 1
    while v <= X:
        p3_pows.append(v)
        v *= p3

    cnt = 0
    for a in p1_pows:
        if a > X: break
        for b in p2_pows:
            ab = a * b
            if ab > X: break
            rem = X // ab
            cnt += bisect.bisect_right(p3_pows, rem)
    return cnt - 1

def solve(p1: int, p2: int, p3: int, k: int) -> int:
    lo, hi = 1, 10**18
    while lo < hi:
        mid = (lo + hi) // 2
        if count_upto(mid, p1, p2, p3) >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    # 입력
    p1, p2, p3, k = map(int, input().split())
    # 풀이
    ans = solve(p1, p2, p3, k)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
