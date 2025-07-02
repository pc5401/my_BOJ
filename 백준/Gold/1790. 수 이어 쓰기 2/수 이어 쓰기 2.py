import sys
input = sys.stdin.readline

def solve(N: int, k: int) -> str:
    length = 1
    start = 1
    while start <= N:
        end = min(N, start * 10 - 1)
        count = end - start + 1
        total_digits = count * length
        if k > total_digits:
            k -= total_digits
            start *= 10
            length += 1
        else:
            idx = (k - 1) // length
            num = start + idx
            if num > N:
                return "-1"
            digit_idx = (k - 1) % length
            return str(num)[digit_idx]
    return "-1"

def main():
    # 입력
    N, k = map(int, input().split())
    # 풀이
    result = solve(N, k)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
