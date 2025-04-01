import sys
input = sys.stdin.readline

def solve(scores: list[int], hongik: int) -> str:
    rank = scores.index(hongik) + 1
    if rank <= 5:
        return "A+"
    elif rank <= 15:
        return "A0"
    elif rank <= 30:
        return "B+"
    elif rank <= 35:
        return "B0"
    elif rank <= 45:
        return "C+"
    elif rank <= 48:
        return "C0"
    else:
        return "F"

def main():
    # 입력
    scores = list(map(int, input().split()))
    hongik = int(input().strip())
    
    # 풀이
    result = solve(scores, hongik)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
