import sys
input = sys.stdin.readline

def solve(n: int, ropes: list[int]) -> int:
    ropes.sort()  # 오름차순 정렬
    result = 0
    for i in range(n):
        candidate = ropes[i] * (n - i)
        result = max(result, candidate)
    return result

def main():
    # 입력
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        ropes = list(map(int, input().split()))
        
        # 풀이
        result = solve(n, ropes)
        
        # 출력
        print(result)

if __name__ == "__main__":
    main()
