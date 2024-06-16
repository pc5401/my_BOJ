import sys
input = sys.stdin.readline


def solve(m: int, d: int) -> int:
    if m < 2:
        return 'Before'
    elif m > 2:
        return 'After'
    
    if d < 18:
        return 'Before'
    elif d > 18:
        return 'After'
    
    return 'Special'


def main():
    # 입력값
    m = int(input())
    d = int(input())

    # 풀이
    result: str = solve(m, d)

    # 출력
    print(result)
if __name__ == "__main__":
    main()
