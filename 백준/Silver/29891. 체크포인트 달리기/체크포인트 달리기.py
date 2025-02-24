import sys
input = sys.stdin.readline

def solve(n: int, k: int, X: list[int]) -> int:
    # Separate checkpoints into left (negative) and right (positive) sides.
    left = [abs(x) for x in X if x < 0]
    right = [x for x in X if x > 0]
    
    left.sort(reverse=True)
    right.sort(reverse=True)
    
    dist = 0
    
    for i in range(0, len(left), k):
        dist += 2 * left[i]
    
    for i in range(0, len(right), k):
        dist += 2 * right[i]
    
    return dist

def main():
    # 입력
    n, k = map(int, input().split())
    X = [int(input()) for _ in range(n)]
    
    # 풀이
    result = solve(n, k, X)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
