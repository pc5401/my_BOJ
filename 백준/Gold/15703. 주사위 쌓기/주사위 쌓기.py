import sys
input = sys.stdin.readline

def solve(n: int, dice: list[int]) -> int:
    dice.sort()
    towers = []
    
    for s in dice:
        candidate_index = -1
        candidate_height = -1
        
        for i, h in enumerate(towers):
            if h <= s and h > candidate_height:
                candidate_index = i
                candidate_height = h
        if candidate_index == -1:
            towers.append(1)
        else:
            towers[candidate_index] += 1
    return len(towers)

def main():
    # 입력
    n = int(input())
    dice = list(map(int, input().split()))
    
    # 풀이
    result = solve(n, dice)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
