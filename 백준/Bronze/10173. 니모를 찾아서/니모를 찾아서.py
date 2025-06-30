import sys
import re
input = sys.stdin.readline

def solve(line: str) -> str:
    return "Found" if re.search(r'nemo', line, re.IGNORECASE) else "Missing"

def main():
    # 입력
    lines = []
    while True:
        line = input().rstrip('\n')
        if line == "EOI":
            break
        lines.append(line)
    # 풀이
    results = [solve(l) for l in lines]
    # 출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
