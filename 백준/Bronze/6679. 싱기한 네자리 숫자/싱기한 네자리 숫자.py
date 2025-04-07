import sys
input = sys.stdin.readline

def digit_sum(n: int, base: int) -> int:
    s = 0
    while n:
        s += n % base
        n //= base
    return s

def solve() -> list[int]:
    result = []
    for num in range(1000, 10000):
        if digit_sum(num, 10) == digit_sum(num, 12) == digit_sum(num, 16):
            result.append(num)
    return result

def main():
    # 풀이
    result = solve()
    # 출력
    for num in result:
        print(num)

if __name__ == "__main__":
    main()
