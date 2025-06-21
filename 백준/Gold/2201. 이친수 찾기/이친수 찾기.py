import sys
input = sys.stdin.readline

def solve(K: int) -> str:
    # 피보나치
    fib = [0, 1, 1]
    while fib[-1] < K:
        fib.append(fib[-1] + fib[-2])
    max_len = len(fib) - 1

    # 길이별 개수 누적합
    ps = [0] * (max_len + 1)
    for i in range(1, max_len + 1):
        ps[i] = ps[i - 1] + fib[i]

    # 사용할 길이 찾기
    L = 1
    while ps[L] < K:
        L += 1
    r = K - ps[L - 1]

    if L == 1:
        return "1"
    if L == 2:
        return "10"

    res = ["1", "0"]
    rem = L - 2
    prev = 0

    for i in range(rem):
        cnt0 = fib[L - 1 - i]
        if r <= cnt0:
            res.append("0")
            prev = 0
        else:
            r -= cnt0
            res.append("1")
            prev = 1

    return "".join(res)

def main():
    # 입력
    K = int(input().strip())
    # 풀이
    ans = solve(K)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
