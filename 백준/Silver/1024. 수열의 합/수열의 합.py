import sys
input = sys.stdin.readline


def solve(n:int, l: int) -> list:

    while l <= 100:
        val = 0
        fst = (n//l) - l
        while val < n:
            val = fst * l + (l*(l-1)/2)
            if val == n:
                return [fst+i for i in range(l)]
            fst += 1

        l += 1
    return [-1]

if __name__ == "__main__":
    N, L = map(int ,input().split())
    res = solve(N, L)
    if res[0] < 0:
        res = [-1]
    print(*res)