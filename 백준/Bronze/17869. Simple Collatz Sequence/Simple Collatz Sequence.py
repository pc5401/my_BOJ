import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n += 1
        steps += 1
    return steps

def main():
    # 입력
    n = int(input().strip())
    # 풀이
    result = solve(n)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
