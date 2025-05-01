import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    # 2 to 64 진법에서 회문인지 검사
    for b in range(2, 65):
        x = n
        digits = []
        while x:
            digits.append(x % b)
            x //= b
        # digits 리스트가 회문인지
        if digits == digits[::-1]:
            return 1
    return 0

def main():
    # 입력
    T = int(input())
    nums = [int(input()) for _ in range(T)]
    # 풀이 & 출력
    out = []
    for n in nums:
        out.append(str(solve(n)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
