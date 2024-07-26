import sys
input = sys.stdin.readline


def solve(A: int, B: int):
    rtn = 0
    l = round(B**(1/2)) + 1
    dp = [1] * l

    for i in range(2, l):
        if not dp[i]:
            continue

        for j in range(i, l, i):
            dp[j] = 0
        
        for k in range(2, l):
            if A <= i**k <= B:
                rtn += 1
            elif i**k > B:
                break
        
    return rtn



def main():
    A, B = map(int, input().split())
    print(solve(A, B))
main()


