import sys
input = sys.stdin.readline

def solve(n: int, m: int, s: list[str], t: list[str], q: int, queries: list[int]) -> list[str]:
    result = []
    for y in queries:
        name = s[(y - 1) % n] + t[(y - 1) % m]
        result.append(name)
    return result

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    
    q = int(input())
    queries = [int(input()) for _ in range(q)]
    
    # 풀이
    result = solve(n, m, s, t, q, queries)
    
    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()