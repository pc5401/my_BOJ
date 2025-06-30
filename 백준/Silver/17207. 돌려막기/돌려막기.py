import sys
input = sys.stdin.readline

def solve(A: list[list[int]], B: list[list[int]]) -> str:
    total = []
    for x in range(5):
        t = 0
        for y in range(5):
            s = 0
            for i in range(5):
                s += A[x][i] * B[i][y]
            t += s
        total.append(t)
    
    # 최소
    mn = min(total)
    names = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]
    # 우선순위
    priority = ["Youngki", "Jinwoo", "Jungwoo", "Junsuk", "Inseo"]
    candidates = [names[i] for i, v in enumerate(total) if v == mn]
    
    for p in priority:
        if p in candidates:
            return p

def main():
    # 입력
    A = [list(map(int, input().split())) for _ in range(5)]
    B = [list(map(int, input().split())) for _ in range(5)]
    # 풀이
    result = solve(A, B)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
