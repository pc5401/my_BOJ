import sys
input = sys.stdin.readline

def solve(schools: list[int]) -> int:
    max_s = max(schools)
    freq = [0] * (max_s + 1)
    for s in schools:
        freq[s] += 1

    cnt = [0] * (max_s + 1)
    # 배수 합을 통해 cnt를 계산
    for T in range(1, max_s + 1):
        for multiple in range(T, max_s + 1, T):
            cnt[T] += freq[multiple]

    ans = 0
    for T in range(1, max_s + 1):
        if cnt[T] >= 2:
            total = T * cnt[T]
            if total > ans:
                ans = total
    return ans

def main():
    # 입력
    N = int(input())
    schools = list(map(int, input().split()))
    # 풀이
    result = solve(schools)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
