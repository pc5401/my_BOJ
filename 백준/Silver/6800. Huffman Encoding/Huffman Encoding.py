import sys

def solve(k, pairs, encoded):
    code_to_char = {code: ch for ch, code in pairs}
    out = []
    buf = []
    for b in encoded:
        buf.append(b)
        s = ''.join(buf)
        if s in code_to_char:
            out.append(code_to_char[s])
            buf.clear()
    return ''.join(out)

def main():
    #입력
    input = sys.stdin.readline
    k = int(input().strip())
    pairs = []
    for _ in range(k):
        ch, code = input().split()
        pairs.append((ch, code))
    encoded = input().strip()
    #풀이
    ans = solve(k, pairs, encoded)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
