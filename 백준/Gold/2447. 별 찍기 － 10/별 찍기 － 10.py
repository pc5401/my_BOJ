import sys
input = sys.stdin.readline

def solve(n: int, memo: dict[int, str]):
    if not n in memo:
        memo[n] = solve(n//3, memo)
    else:
        return memo[n]

    w = memo[n].split('\n')
    rtn = []
    m = n // 3
    for i in range(m):
        rtn.append(w[i] * 3)

    for i in range(m):
        rtn.append(w[i] + (' '*m) + w[i]) 

    for i in range(m):
        rtn.append(w[i] * 3)

    return '\n'.join(rtn)

def main():
    N = int(input())
    memo = {1 :'*'}
    print(solve(N, memo))

main()