import sys
input = sys.stdin.readline

def solve(value: int, check: int) -> str:
    ones = bin(value).count('1')
    expected = ones % 2  
    return "Valid" if expected == check else "Corrupt"

def main():
    # 입력
    data = input().split()
    T = int(data[0])
    tests = [tuple(map(int, input().split())) for _ in range(T)]
    # 풀이
    results = [solve(v, c) for v, c in tests]
    # 출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
