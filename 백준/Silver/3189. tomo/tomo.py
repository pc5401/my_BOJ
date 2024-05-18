import sys
input = sys.stdin.readline


def solve(A: int, B: int, C: int) -> int:
    cnt = 1
    cut = 10 ** len(str(C))
    visited = set()
    number = (A*B) % cut
    while True:
        if number in visited:
            return 0
        visited.add(number)
        if number == C:
            return cnt
        
        number = (number * B) % cut
        cnt += 1



def main():
    # 입력값
    A, B, C = map(int, input().split())
    A: int
    B: int
    C: int
    
    # 풀이 & 출력
    result: int = solve(A, B, C)

    print(result if result else 'NIKAD')
    
if __name__ == "__main__":
    main()

