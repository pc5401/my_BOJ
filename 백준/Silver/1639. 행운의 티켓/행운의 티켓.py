import sys
input = sys.stdin.readline


def solve(N: int, S: str) -> int:
    rtn = 0

    for n in range(N):
        left, right = 0, 0
        i, j = n, n + 1
        while i >= 0 and j < N:
            left += int(S[i])
            right += int(S[j])
            if left == right:
                rtn = max(rtn, j - i + 1)
            i -= 1
            j += 1
        
    return rtn


def main():
    # 입력값
    S = input().rstrip()

    # 풀이
    result: list[int] = solve(len(S), S)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()

