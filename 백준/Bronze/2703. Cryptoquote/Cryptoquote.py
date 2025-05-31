import sys
input = sys.stdin.readline

def solve(cipher: str, rule: str) -> str:
    res = []
    for ch in cipher:
        if ch == ' ':
            res.append(' ')
        else:
            idx = ord(ch) - ord('A')
            res.append(rule[idx])
    return "".join(res)

def main():
    # 입력
    T = int(input())
    # 풀이
    for _ in range(T):
        cipher = input().rstrip('\n')
        rule = input().rstrip('\n')
        result = solve(cipher, rule)
        # 출력
        print(result)

if __name__ == "__main__":
    main()
