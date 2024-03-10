import sys
input = sys.stdin.readline


def solve(A: str, B: str) -> int:
    L = A.count('L') + B.count('L')
    O = A.count('O') + B.count('O')
    V = A.count('V') + B.count('V')
    E = A.count('E') + B.count('E')

    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

def main():
    main_name = input().rstrip()
    N = int(input())
    names = [input().rstrip() for _ in range(N)]
    res = [(solve(main_name, name), name )for name in names]
    res.sort(key=lambda x: (-x[0], x[1]))

    print(res[0][1])

if __name__ == "__main__":
    main()
