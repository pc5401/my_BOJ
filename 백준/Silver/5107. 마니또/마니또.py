import sys
import collections
input = sys.stdin.readline

def find(m):
    if union_find[m] != m:
        union_find[m] = find(union_find[m])
    return union_find[m]


def solve(n: int, lst: list, union_find: collections.defaultdict ) -> int:
    
    for a, b in lst:
        A, B = find(a), find(b)
        if A != B:
            union_find[A] = B

    cnt = { i for i in union_find.values()}
    return len(cnt)


if __name__ == "__main__":
    T = 0
    while 1:
        N = int(input())
        if not N:
            break

        union_find = collections.defaultdict(str)
        lst = []
        for n in range(1, N+1):
            a, b  = input().split()
            lst.append((a,b))
            union_find[a] = a
        
        res = solve(N, lst, union_find)
        T += 1
        print(T, res)

