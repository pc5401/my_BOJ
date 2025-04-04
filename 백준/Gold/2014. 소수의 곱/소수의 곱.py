import sys, heapq
input = sys.stdin.readline

def solve(K: int, N: int, primes: list[int]) -> int:
    heap = []
    visited = set()
    for p in primes:
        heapq.heappush(heap, p)
        visited.add(p)
    result = 0
    for _ in range(N):
        result = heapq.heappop(heap)
        for p in primes:
            nxt = result * p
            if nxt not in visited:
                visited.add(nxt)
                heapq.heappush(heap, nxt)
            if result % p == 0:
                break
    return result

def main():
    # 입력
    K, N = map(int, input().split())
    primes = list(map(int, input().split()))
    
    # 풀이
    result = solve(K, N, primes)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
