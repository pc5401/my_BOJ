import sys
input = sys.stdin.readline

def solve(M: int, N: int) -> list[int]:
    result = [0] * 10
    for num in range(M, N + 1):
        for ch in str(num):
            result[ord(ch) - ord('0')] += 1
    return result

def main():
    # 입력
    M, N = map(int, input().split())
    
    # 풀이
    result = solve(M, N)
    
    # 출력
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
