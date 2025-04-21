import sys
input = sys.stdin.readline

def solve(N: int, K: int, cables: list[int]) -> int:
    lo, hi = 1, max(cables)
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 0
        for length in cables:
            cnt += length // mid
        if cnt >= K:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

def main():
    # 입력
    N, K = map(int, input().split())
    cables = []
    for _ in range(N):
        s = input().strip()
        # "X.YY" 형태 → 정수 센티미터 단위로 변환
        whole, frac = s.split('.')
        length_cm = int(whole) * 100 + int(frac)
        cables.append(length_cm)
    
    # 풀이
    best_cm = solve(N, K, cables)
    
    # 출력
    if best_cm <= 0:
        print("0.00")
    else:
        meters = best_cm // 100
        cents = best_cm % 100
        print(f"{meters}.{cents:02d}")

if __name__ == "__main__":
    main()
