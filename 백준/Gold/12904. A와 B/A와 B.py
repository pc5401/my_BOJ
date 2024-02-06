import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solve(S: str, T: str) -> int:
    if len(S) == len(T):
        if S == T:
            return 1
        else:
            return 0

    if T[-1] == 'A' and solve(S, T[:-1]):
        return 1
    elif T[-1] == 'B' and solve(S, T[:-1][::-1]):
        return 1
    else:
        return 0 

if __name__ == '__main__':
    S = input().rstrip()
    T = input().rstrip()
    print(solve(S, T))
