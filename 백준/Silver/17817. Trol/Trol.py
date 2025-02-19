import sys
input = sys.stdin.readline

def solve(q: int, lr: list[list[int]]) -> list[int]:
    ps = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    
    def S(n: int) -> int:
        return (n // 9) * 45 + ps[n % 9]
    
    result = []
    for l, r in lr:
        result.append(S(r) - S(l - 1))
    return result

def main():
    # 입력
    Q = int(input())
    lr = [list(map(int, input().split())) for _ in range(Q)]
    
    # 풀이
    result = solve(Q, lr)
    
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
