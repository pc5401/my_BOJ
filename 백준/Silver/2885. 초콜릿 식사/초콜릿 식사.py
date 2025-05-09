import sys
input = sys.stdin.readline

def solve(K: int) -> tuple[int,int]:
    n = 0
    while (1 << n) < K:
        n += 1
    D = 1 << n

    cnt = [0] * (n + 1)
    cnt[n] = 1
    splits = 0
    # K의 각 비트 처리
    for i in range(n + 1):
        if (K >> i) & 1:
            if cnt[i] > 0:
                cnt[i] -= 1
            else:
                # 위쪽에서 조각 내려받기
                j = i + 1
                while j <= n and cnt[j] == 0:
                    j += 1
                # j에서 i로 갈 때마다 쪼개기
                for k in range(j, i, -1):
                    cnt[k] -= 1
                    cnt[k-1] += 2
                    splits += 1
                cnt[i] -= 1  # 하나 사용

    return D, splits

def main():
    # 입력
    K = int(input())
    # 풀이
    D, result = solve(K)
    # 출력
    print(D, result)

if __name__ == "__main__":
    main()
