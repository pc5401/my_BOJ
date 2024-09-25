import sys
input = sys.stdin.readline


def solve(word: str) -> int:
    
    stack = []

    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    return 0 if stack else 1

def main():
    # 입력값
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    
    # 풀이
    result = 0
    for word in words:
        result += solve(word)

    # 출력
    print(result)


if __name__ == "__main__":
    main()


