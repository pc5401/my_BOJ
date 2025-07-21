import sys
input = sys.stdin.readline

def solve(words: list[str]) -> str:
    ignore = {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"}
    abbr = []
    for idx, w in enumerate(words):
        if idx != 0 and w in ignore:
            continue
        abbr.append(w[0].upper())
    return "".join(abbr)

def main():
    # 입력
    line = input().strip().split()
    # 풀이
    result = solve(line)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
