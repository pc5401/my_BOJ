import sys
input = sys.stdin.readline

def solve(B: int, D: str) -> int:
    mod = B - 1
    total = 0
    for ch in D:
        total = (total + int(ch, B)) % mod
    return total

def main():
    # 입력
    T = int(input().strip())
    # 풀이 & 출력
    for _ in range(T):
        B, D = input().split()
        B = int(B)
        D = D.strip()
        result = solve(B, D)
        print(result)

if __name__ == "__main__":
    main()
