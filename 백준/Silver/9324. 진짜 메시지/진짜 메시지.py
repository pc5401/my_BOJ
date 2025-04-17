import sys
input = sys.stdin.readline

def solve(M: str) -> bool:
    counts = [0] * 26
    i = 0
    L = len(M)
    while i < L:
        c = M[i]
        idx = ord(c) - ord('A')
        counts[idx] += 1
        if counts[idx] % 3 == 0:
            if i + 1 >= L or M[i+1] != c:
                return False
            i += 1
        i += 1
    return True

def main():
    # 입력
    t = int(input().strip())
    # 풀이 & 출력
    for _ in range(t):
        M = input().rstrip('\n')
        result = "OK" if solve(M) else "FAKE"
        # 출력
        print(result)

if __name__ == "__main__":
    main()
