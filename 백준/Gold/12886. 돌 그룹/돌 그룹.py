import sys
import collections
input = sys.stdin.readline

def XY(x, y, Z) -> tuple:
    X = min(x, y)
    Y = max(x, y)
    return (X+X, Y-X, Z)

def solve(A: int, B: int, C: int) -> int:
    if A == B and B == C:
        return 1
    
    visited = set()
    visited.add((A,B,C))
    Q = collections.deque()
    Q.append((A,B,C))
    
    while Q:
        a,b,c = Q.popleft()
        lst = []

        if a != b:
            lst.append(XY(a, b, c))
        if b != c:
            lst.append(XY(b, c, a))
        if a != c:
            lst.append(XY(a, c, b))

        for v in lst:
            if v in visited:
                continue
            visited.add(v)
            Q.append(v)
            if v[0] == v[1] and v[0] == v[2]:
                return 1

    return 0



if __name__ == "__main__":
    A, B, C = map(int, input().split())
    total = (A+B+C)
    if total % 3:
        print(0)
    else:
        print(solve(A,B,C))


