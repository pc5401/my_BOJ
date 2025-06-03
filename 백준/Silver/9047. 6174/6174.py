import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    target = 6174
    cnt = 0
    x = n
    while x != target:
        s = f"{x:04d}"
        a = int("".join(sorted(s, reverse=True)))
        b = int("".join(sorted(s)))
        x = a - b
        cnt += 1
    return cnt

def main():
    # 입력
    T = int(input())
    nums = [int(input()) for _ in range(T)]
    # 풀이
    results = [solve(n) for n in nums]
    # 출력
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
