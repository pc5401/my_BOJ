import sys
input = sys.stdin.readline

def solve(N, R1, C1, R2, C2):
    S = 2 * N - 1
    center = N - 1
    out_lines = []
    for r in range(R1, R2 + 1):
        i = r % S
        rd = abs(i - center)
        k = center - rd
        row_chars = []
        for c in range(C1, C2 + 1):
            j = c % S
            dd = abs(j - center)
            if dd > k:
                row_chars.append('.')
            else:
                ch = (rd + dd) % 26
                row_chars.append(chr(ord('a') + ch))
        out_lines.append(''.join(row_chars))
    return out_lines

def main():
    # 입력
    N, R1, C1, R2, C2 = map(int, input().split())

    # 풀이
    result = solve(N, R1, C1, R2, C2)

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
