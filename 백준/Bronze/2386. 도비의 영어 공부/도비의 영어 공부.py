import sys

def solve(lines):
    result = []
    for line in lines:
        line = line.rstrip('\n')
        if line == '#':
            break
        ch, sentence = line.split(' ', 1)
        cnt = sentence.lower().count(ch.lower())
        result.append(f"{ch} {cnt}")
    return result

def main():
    #입력
    input = sys.stdin.readline
    lines = [line for line in sys.stdin]

    #풀이
    ans = solve(lines)

    #출력
    print("\n".join(ans))

if __name__ == "__main__":
    main()
