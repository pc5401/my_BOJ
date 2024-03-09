
from typing import List
import math

def is_parallelogram_possie(A: tuple, B: tuple, C: tuple) -> bool:
    if (A[0] == B[0] and C[0] == A[0]) or (A[1] == B[1] and C[1] == A[1]):
        return False
    
    BA_x_line = B[0] - A[0]
    BA_y_line = B[1] - A[1]
    
    CA_x_line = C[0] - A[0]
    CA_y_line = C[1] - A[1]

    BA = BA_y_line / BA_x_line if BA_x_line != 0 else float('INF')
    CA = CA_y_line / CA_x_line if CA_x_line != 0 else float('INF')
    if BA == CA:
        return False

    return True


def pythagoras(X: tuple, Y: tuple) -> float:
    return math.sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)

def get_line_length(target: tuple, A: tuple, B: tuple) -> float:
    return 2 * (pythagoras(target, A) + pythagoras(target, B))

def main():
    A_x, A_y, B_x, B_y, C_x, C_y = map(int, input().split())
    A, B, C = (A_x, A_y), (B_x, B_y), (C_x, C_y)
    if is_parallelogram_possie(*sorted((A, B, C))):

        a = get_line_length(A, B, C)
        b = get_line_length( B, C, A)
        c = get_line_length(C, A, B)
        print(max(a,b,c) - min(a,b,c))
    else:
        print(-1.0)


if __name__ == "__main__":
    main()