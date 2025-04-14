import sys
input = sys.stdin.readline

def solve(n: int, filenames: list[str]) -> int:
    count = 0
    for fname in filenames:
        if fname.count('.') != 1:
            continue
        file_part, ext_part = fname.split('.')
        if not file_part or not ext_part:
            continue
        if len(file_part) > 8 or len(ext_part) > 3:
            continue
        if not (file_part.isalpha() and ext_part.isalpha()):
            continue
        count += 1
    return count

def main():
    # 입력
    n = int(input().strip())
    filenames = [input().strip() for _ in range(n)]
    
    # 풀이
    result = solve(n, filenames)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
