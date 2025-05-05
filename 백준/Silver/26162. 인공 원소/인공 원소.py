import sys
input = sys.stdin.readline

def solve(a: int, primes: list[bool]) -> bool:
    for p in range(2, a // 2 + 1):
        if primes[p] and primes[a - p]:
            return True
    return False

def main():
    # 입력
    N = int(input())
    queries = [int(input()) for _ in range(N)]
    
    max_a = 118
    is_prime = [False, False] + [True] * (max_a - 1)
    for i in range(2, int(max_a**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_a + 1, i):
                is_prime[j] = False
    # 풀이 & 출력
    for a in queries:
        print("Yes" if solve(a, is_prime) else "No")

if __name__ == "__main__":
    main()
