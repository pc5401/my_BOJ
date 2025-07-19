import sys
input = sys.stdin.readline

def solve(seq: str) -> int:
    pending_L = 0
    pending_S = 0
    total = 0
    for c in seq:
        if c.isdigit():
            total += 1
        elif c == 'L':
            pending_L += 1
        elif c == 'S':
            pending_S += 1
        elif c == 'R':
            if pending_L > 0:
                pending_L -= 1
                total += 1
            else:
                break
        elif c == 'K':
            if pending_S > 0:
                pending_S -= 1
                total += 1
            else:
                break
    return total

def main():
    # 입력
    n = int(input().strip())
    seq = input().strip()
    # 풀이
    result = solve(seq)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
