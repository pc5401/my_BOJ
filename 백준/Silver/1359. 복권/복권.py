import sys
import math
input = sys.stdin.readline


def solve(n: int, m: int, k: int) -> int:
    total_sample = math.comb(n, m) 
    cnt = 0
    for i in range(k, m+1): # k 개 이상의 번호가 뽑힌 경우들
        cnt += math.comb(m, i) * math.comb(n-m, m-i)

    return cnt / total_sample


def main():
    # 입력값
    N, M, K = map(int, input().split())
    N: int
    M: int
    K: int
    # 풀이
    result = solve(N, M, K)
    # 출력
    print(result)


if __name__ == "__main__":
    main()