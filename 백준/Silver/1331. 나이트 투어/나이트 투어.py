import sys
input = sys.stdin.readline


def is_possible_movement(A: list, B: list) -> bool:
    movement = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]

    for m in movement:
        if (A[0] + m[0]) == B[0] and (A[1] + m[1]) == B[1]:
            return True
    
    return False


def solve(knights: list[str]) -> bool:
    chessboard = [[0]*6 for _ in range(6)]

    for i in range(36):
        r, c = knights[i]
        chessboard[r][c] += 1

        if i and not is_possible_movement(knights[i-1], knights[i]):
            return False
    
    for i in range(6):
        for j in range(6):
            if chessboard[i][j] != 1:
                return False
    
    if not is_possible_movement(knights[35], knights[0]):
        return False

    return True
    

def main():
    knights = [list(map(lambda x : int(x)-1 if x.isdigit() else ord(x) - 65 ,input().rstrip())) for _ in range(36)]
    print( 'Valid' if solve(knights) else 'Invalid')

if __name__ == "__main__":
    main()
