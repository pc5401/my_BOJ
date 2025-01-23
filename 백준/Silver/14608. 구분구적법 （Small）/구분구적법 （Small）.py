import sys
input = sys.stdin.readline


def solve(K: int, terms: list[int], a: int, b: int, N: int) -> str:
    c1, c2 = terms # 1차 항까지만,

    value = (c1 * (b**2 - a**2) / 2.0) + (c2 * (b - a))

    X = (b - a) / float(N)
    C = X * (c1*(N*a + (N*(N-1)/2.0)*X) + c2*N)
    M = c1 * N * X
    if abs(M) < 1e-15:
        return "-1"
    
    
    eps = (value - C) / M
    
    if 0 <= eps <= X:
        return f"{eps:.4f}"
    else:
        return "-1"
    

def main():
    # 입력
    K = int(input())
    terms = list(map(int, input().split()))
    a, b, N = map(int, input().split())

    # 풀이 & 출력
    print(solve(K, terms, a, b, N))
    

if __name__ == "__main__":
    main()
