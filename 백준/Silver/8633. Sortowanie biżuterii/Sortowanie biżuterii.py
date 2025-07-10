import sys
input = sys.stdin.readline

def solve(lst: list[str]) -> list[str]:
    return sorted(lst, key=lambda x: (len(x), x))

def main():
    # 입력
    N = int(input().strip())
    lst = [input().strip() for _ in range(N)]
    # 풀이
    result = solve(lst)
    # 출력
    print('\n'.join(result))

if __name__ == "__main__":
    main()