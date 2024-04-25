import sys
input = sys.stdin.readline


def solve(S: int) -> int:
    N = len(S)

    if S == S[::-1]:
        return N
    
    for i in range(1, N):
        word = S + S[:i][::-1]
        if word == word[::-1]:
            return len(word)
    
    return 2 * N


def main():
    # 입력값
    S: str = input().rstrip()
    # 풀이
    result: int = solve(S)
    # 출력
    print(result)


if __name__ == "__main__":
    main()