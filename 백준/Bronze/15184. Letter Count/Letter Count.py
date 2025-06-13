import sys
input = sys.stdin.readline

def solve(s: str) -> list[str]:
    # 알파벳 빈도 세기
    freq = {chr(ord('A') + i): 0 for i in range(26)}
    for ch in s:
        if ch.isalpha():
            freq[ch.upper()] += 1

    lines = []
    for i in range(26):
        letter = chr(ord('A') + i)
        stars = '*' * freq[letter]
        lines.append(f"{letter} | {stars}")
    return lines

def main():
    # 입력
    s = input().rstrip('\n')
    # 풀이
    result = solve(s)
    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
