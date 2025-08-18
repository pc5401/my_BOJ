import sys
input = sys.stdin.readline

def solve(S, P):
    cntS = [0] * 26
    cntP = [0] * 26
    for ch in S:
        cntS[ord(ch) - 97] += 1
    for ch in P:
        cntP[ord(ch) - 97] += 1
    for i in range(26):
        if cntS[i] < cntP[i]:
            return "NO"
    return "YES"

def main():
    # 입력
    S = input().strip()
    P = input().strip()

    # 풀이
    result = solve(S, P)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
