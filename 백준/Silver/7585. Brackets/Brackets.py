import sys
input = sys.stdin.readline

def solve(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

def main():
    # 입력
    while True:
        line = input().rstrip('\n')
        if line == "#":
            break
        # 풀이
        result = solve(line)
        # 출력
        print("Legal" if result else "Illegal")

if __name__ == "__main__":
    main()
