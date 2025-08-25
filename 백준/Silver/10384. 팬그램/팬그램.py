def solve(s):
    cnt = [0] * 26
    for ch in s:
        o = ord(ch)
        if 65 <= o <= 90:
            cnt[o - 65] += 1
        elif 97 <= o <= 122:
            cnt[o - 97] += 1
    m = min(cnt)
    if m >= 3:
        return "Triple pangram!!!"
    if m >= 2:
        return "Double pangram!!"
    if m >= 1:
        return "Pangram!"
    return "Not a pangram"

def rtn(n, lines):
    out = []
    for i in range(n):
        out.append(f"Case {i+1}: {solve(lines[i])}")
    return out

def main():
    # 입력
    n = int(input().strip())
    lines = [input().rstrip('\n') for _ in range(n)]

    # 풀이
    result = rtn(n, lines)

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()