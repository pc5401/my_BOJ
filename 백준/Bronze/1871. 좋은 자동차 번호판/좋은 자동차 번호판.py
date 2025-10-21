import sys
import re

PAT = re.compile(r'^([A-Z]{3})-([0-9]{4})$')

def letters_value(s: str) -> int:
    return (ord(s[0]) - 65) * 26 * 26 + (ord(s[1]) - 65) * 26 + (ord(s[2]) - 65)

def solve(N, plates):
    res = []
    for p in plates:
        m = PAT.fullmatch(p.strip())
        if not m:
            res.append("not nice")
            continue
        letters, digits = m.groups()
        valL = letters_value(letters)
        valD = int(digits)  # leading zeros ok
        res.append("nice" if abs(valL - valD) <= 100 else "not nice")
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    # 입력
    N = int(data[0].strip())
    plates = data[1:1+N]
    # 풀이
    ans_lines = solve(N, plates)
    # 출력
    print("\n".join(ans_lines))

if __name__ == "__main__":
    main()
