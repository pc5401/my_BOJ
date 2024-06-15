import sys
input = sys.stdin.readline


def solve(s: str, f: str) -> int:
    s_list = list(ord(i) for i in s)
    f_set = set(ord(i) for i in f)
    rtn = 0

    for sv in s_list:
        minV = float('inf')
        for fv in f_set:
            diff = abs(sv - fv)
            minV = min(diff, 26 - diff, minV)
        rtn += minV
    
    return rtn


def main():
    # 입력값
    T = int(input())
    S, F = [], []
    for _ in range(T):
        S.append(input().rstrip())
        F.append(input().rstrip())
    # 풀이
    result = [solve(S[t], F[t]) for t in range(T)]

    # 출력
    for num, res in enumerate(result, start=1):
        print(f'Case #{num}: {res}')

if __name__ == "__main__":
    main()