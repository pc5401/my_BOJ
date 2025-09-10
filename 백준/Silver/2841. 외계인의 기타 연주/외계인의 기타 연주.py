import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(N, P, notes):
    stacks = defaultdict(list)
    moves = 0
    for s, f in notes:
        st = stacks[s]
        while st and st[-1] > f:
            st.pop()
            moves += 1
        if not st or st[-1] < f:
            st.append(f)
            moves += 1
        
    return moves

def main():
    # 입력
    N, P = map(int, input().split())
    notes = [tuple(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(N, P, notes)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
