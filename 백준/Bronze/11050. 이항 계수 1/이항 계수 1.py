import sys
input = sys.stdin.readline

def facto(n) -> int:
    if n <= 1:
        return 1
    return n * facto(n-1)

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(facto(N)//(facto(K)*facto(N-K)))